from datetime import datetime, timezone

from django.contrib.auth.models import User
from django.db import models as models
from . import managers
from .utils import get_related_objects
from django.utils import timezone


class SayaraModel(models.Model):
    date_created = models.DateTimeField(default=timezone.now, )
    date_modified = models.DateTimeField(default=timezone.now)
    date_removed = models.DateTimeField(null=True, blank=True)

    objects = managers.LogicalDeletedManager()

    def active(self):
        return self.date_removed is None

    active.boolean = True

    def delete(self):
        # Fetch related models
        to_delete = get_related_objects(self)

        for obj in to_delete:
            obj.delete()

        # Soft delete the object
        self.date_removed = timezone.now()
        self.save()

    class Meta:
        abstract = True


class Image(SayaraModel):
    image = models.ImageField(upload_to="images/vehicules",
                              default='images/vehicules/voiture.jpg')


class Vehicule(SayaraModel):
    # Fields
    app_label = "Vehicule"
    num = models.CharField(max_length=100)

    @property
    def marque(self):
        return self.versionVoiture.modele.nom.marque

    @property
    def version(self):
        return self.versionVoiture.nom

    @property
    def modele_name(self):
        return self.versionVoiture.modele.nom

    class Meta:
        abstract = True

    def __str__(self):
        return self.num


class Marque(SayaraModel):
    # Fields
    app_label = "Marque"
    nom = models.CharField(max_length=50)
    image = models.ImageField(default='images/vehicules/voiture.jpg',
                              upload_to="marque/images/")

    def __str__(self):
        return self.nom

    # TODO change this to real fabricant id
    @property
    def fabricant_id(self):
        return 1


class RefVersion(SayaraModel):
    nom = models.CharField(max_length=255, unique=True, primary_key=True)

    def __str__(self):
        return self.nom


class Version(SayaraModel):
    # Fields
    app_label = "Version"
    code = models.CharField(max_length=20, primary_key=True)
    ref = models.ForeignKey(RefVersion, on_delete=models.CASCADE)
    options = models.ManyToManyField('SayaraApi.Option', blank=True)
    modele = models.ForeignKey('SayaraApi.Modele', on_delete=models.CASCADE)
    prix_base = models.IntegerField()
    ficheTechnique = models.ForeignKey("SayaraApi.FicheTechnique",
                                       on_delete=models.CASCADE)
    couleur = models.ManyToManyField("SayaraApi.Couleur")

    image1 = models.ImageField(upload_to="images/vehicules",
                               default='images/vehicules/voiture.jpg')
    image2 = models.ImageField(upload_to="images/vehicules",
                               default='images/vehicules/voiture.jpg')
    image3 = models.ImageField(upload_to="images/vehicules",
                               default='images/vehicules/voiture.jpg')

    @property
    def fabricantVersion_id(self):
        return self.modele.ref.marque

    @property
    def modele_name(self):
        return self.modele.ref.nom

    @property
    def marque_name(self):
        return self.modele.ref.marque.nom

    @property
    def prix(self):
        query = TarifVersion.objects.filter(version=self, base=False,
                                            debut__lte=datetime.now(),
                                            fin__gte=datetime.now()).first()
        if query:
            return query.prix
        query = TarifVersion.objects.filter(version=self, base=True).last()
        if query:
            return query.prix
        return 0

    @property
    def nom(self):
        return self.ref.nom

    def __str__(self):
        return self.ref.nom


class RefModele(SayaraModel):
    nom = models.CharField(max_length=255, unique=True)
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Modele(SayaraModel):
    # Fields
    app_label = "Modele"
    code = models.CharField(max_length=10)
    ref = models.ForeignKey(RefModele, related_name="modele",
                            on_delete=models.CASCADE)
    image = models.ImageField(default='images/vehicules/voiture.jpg',
                              upload_to="images/vehicules")

    def __str__(self):
        return self.ref.nom

    @property
    def nom(self):
        return self.ref.nom



    @property
    def fabricant_nom(self):
        return self.nom.marque.fabricant

    @property
    def fabricant_pk(self):
        return self.ref.marque

    @property
    def marque_nom(self):
        return self.ref.marque.nom

    @property
    def marqueId(self):
        return self.ref.marque.pk

    @classmethod
    def create(cls, new_ref):
        book = cls()
        print(new_ref)
        # do something with the book
        return book


class Annonce(SayaraModel):
    # Fields
    app_label = "Annonce"
    # idAnnonce = models.AutoField(primary_key=True)

    titre = models.CharField(max_length=50)
    prix = models.IntegerField()
    commentaires = models.CharField(max_length=255)

    # Relationship Fields
    vehicule = models.ForeignKey('SayaraApi.VehiculeOccasion',
                                 on_delete="DO_NOTHING", )
    user = models.ForeignKey(User, related_name="proprietaire",
                             on_delete="DO_NOTHING")

    @property
    def couleur(self):
        return self.vehicule.couleur

    @property
    def version_name(self):
        return self.vehicule.version.nom

    @property
    def marque_name(self):
        return self.vehicule.marque_name

    @property
    def modele_name(self):
        return self.vehicule.modele_name

    @property
    def image1(self):
        return self.vehicule.image1

    @property
    def image2(self):
        return self.vehicule.image2

    @property
    def image3(self):
        return self.vehicule.image3

    @property
    def kilometrage(self):
        return self.vehicule.kilometrage

    @property
    def pseudoUser(self):
        return self.user.username

    @property
    def date(self):
        return self.vehicule.date

    def __str__(self):
        return self.titre


class Fabricant(SayaraModel):
    app_label = "fabricant"
    # Fields
    nom = models.CharField(max_length=255)

    # Relationship Fields
    marque = models.ForeignKey(
        'SayaraApi.Marque',
        on_delete=models.CASCADE, related_name="fabricants",
    )

    def __str__(self):
        return self.nom


class Profile(SayaraModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    is_fabricant = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    fabricant = models.ForeignKey(
        'SayaraApi.fabricant',
        on_delete=models.CASCADE, related_name="fabricant", blank=True,
        null=True
    )

    def __str__(self):
        if self.is_fabricant:
            return self.fabricant.nom
        return self.user.username


class RefCouleur(SayaraModel):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom


class Couleur(SayaraModel):
    app_label = "Couleur"
    code = models.CharField(max_length=3)
    ref = models.ForeignKey(RefCouleur, on_delete=models.CASCADE)

    modele = models.ForeignKey(
        'SayaraApi.Modele',
        on_delete=models.CASCADE, blank=False, null=False
    )

    def __str__(self):
        return self.ref.nom

    @property
    def nom(self):
        return self.ref.nom

    @property
    def fabricantCouleur_id(self):
        return self.modele.fabricantModele_id

    @property
    def prix(self):
        query = TarifCouleur.objects.filter(couleur=self, base=False,
                                            debut__lte=datetime.now(),
                                            fin__gte=datetime.now()).first()
        if query:
            return query.prix
        query = TarifCouleur.objects.filter(couleur=self, base=True).last()
        if query:
            return query.prix
        return 0


class RefOption(SayaraModel):
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom


class Option(SayaraModel):
    # Fields
    ref = models.ForeignKey(RefOption, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, primary_key=True)
    modele = models.ForeignKey('SayaraApi.modele', on_delete=models.CASCADE)

    # def save(self, fabricantOption_id=None, *args, **kwargs):
    #     print(fabricantOption_id, args, kwargs)
    #     # if not self.pk:
    #     #     self.fabricantOption_id=fabricant.objects.get(pk=1)
    #     super(Option, self).save(*args, **kwargs)
    def __str__(self):
        return self.ref.nom

    @property
    def prix(self):
        query = TarifOption.objects.filter(option=self, base=False,
                                           debut__lte=datetime.now(),
                                           fin__gte=datetime.now()).first()
        if query:
            return query.prix
        query = TarifOption.objects.filter(option=self, base=True).last()
        if query:
            return query.prix
        return 0

    @property
    def nom(self):
        return self.ref.nom


class VehiculeOccasion(SayaraModel):
    kilometrage = models.IntegerField()
    date = models.DateField()
    image1 = models.ImageField(upload_to="images/vehicules",
                               default='images/vehicules/voiture.jpg')
    image2 = models.ImageField(upload_to="images/vehicules",
                               default='images/vehicules/voiture.jpg')
    image3 = models.ImageField(upload_to="images/vehicules",
                               default='images/vehicules/voiture.jpg')
    version = models.ForeignKey(RefVersion, related_name="Refversion",
                                on_delete="DO_NOTHING")
    modele = models.ForeignKey(RefModele, related_name="RefModele",
                               on_delete="DO_NOTHING")
    options = models.ManyToManyField(RefOption, blank=True)
    couleur = models.CharField(max_length=100)

    # options = models.ManyToManyField(RefOption, related_name="options", blank=True)

    @property
    def marque_name(self):
        return self.modele.marque.nom

    @property
    def modele_name(self):
        return self.modele.nom


class VehiculeNeuf(Vehicule):
    disponible = models.BooleanField()
    reserve = models.BooleanField()
    concessionnaire = models.CharField(max_length=250)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)
    options = models.ManyToManyField(Option, blank=True)
    couleur = models.ForeignKey(Couleur, on_delete=models.CASCADE)

    # TODO Contrainte : Option incluses dans options version
    # TODO Contrainte : Couleur incluses dans couleurs Version
    @property
    def prix(self):
        return 122

    @property
    def marque(self):
        return self.version.modele.ref.marque

    @property
    def fabricant_id(self):
        return 1

    @property
    def fabricant_name(self):
        return "Notfixedyet"

    @property
    def image1(self):
        return self.version.image1

    @property
    def modele_name(self):
        return self.version.modele_name

    @property
    def modele(self):
        return self.version.modele

    @property
    def titre(self):
        return str(self.modele_name + " " + self.version.nom)


class TarifOption(SayaraModel):
    debut = models.DateField()
    fin = models.DateField()
    prix = models.FloatField()
    base = models.BooleanField(default=False)
    # Relationship Fields
    option = models.ForeignKey(Option, on_delete=models.CASCADE,
                               related_name="lignetarifs")

    @property
    def valid(self):
        return self.debut <= datetime.now() <= self.fin

    def __str__(self):
        return self.option.nom

    class Meta:
        ordering = ('-fin',)


class TarifVersion(SayaraModel):
    debut = models.DateField()
    fin = models.DateField()
    prix = models.FloatField()
    base = models.BooleanField(default=False)
    # Relationship Fields
    version = models.ForeignKey(Version, on_delete=models.CASCADE,
                                related_name="lignetarifs")

    @property
    def valid(self):
        return self.debut <= datetime.now() < self.fin

    class Meta:
        ordering = ('-fin', 'version',)


class TarifCouleur(SayaraModel):
    debut = models.DateField()
    fin = models.DateField()
    prix = models.FloatField()
    base = models.BooleanField(default=False)
    # Relationship Fields
    couleur = models.ForeignKey(Couleur, on_delete=models.CASCADE, blank=True,
                                null=True)

    @property
    def valid(self):
        return self.debut <= datetime.now() < self.fin

    class Meta:
        ordering = ('-fin', 'couleur',)


class LigneTarif(SayaraModel):
    # Fields
    dateDebut = models.DateField()
    dateFin = models.DateField()
    prix = models.FloatField()


class FicheTechnique(SayaraModel):
    nombrePortes = models.IntegerField()
    boiteVitesse = models.CharField(max_length=100)
    puissanceFiscale = models.CharField(max_length=100)
    motorisation = models.CharField(max_length=100)
    consommation = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    capaciteReservoir = models.CharField(max_length=100)
    vitesseMaxi = models.IntegerField()
    acceleration = models.CharField(max_length=100)

    @property
    def version_fiche(self):
        return self.version_set


class Offre(SayaraModel):
    annonce = models.ForeignKey(Annonce, on_delete=models.DO_NOTHING)
    prix = models.IntegerField()
    user = models.ForeignKey(User, related_name="offrant",
                             on_delete="DO_NOTHING")


class Commande(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(VehiculeNeuf, on_delete=models.CASCADE)
    confirmation = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
