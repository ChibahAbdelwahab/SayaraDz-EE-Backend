from datetime import datetime

from django.contrib.auth.models import User
from django.db import models as models


class Image(models.Model):
    image = models.ImageField(upload_to="images/vehicules", default='images/vehicules/voiture.jpg')


class Vehicule(models.Model):
    # Fields
    app_label = "Vehicule"
    num = models.CharField(max_length=100)
    vehicule = models.AutoField(primary_key=True)

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


class Marque(models.Model):
    # Fields
    app_label = "Marque"
    nom = models.CharField(max_length=50)
    image = models.ImageField(default='images/vehicules/voiture.jpg', upload_to="marque/images/")

    def __str__(self):
        return self.nom

    # TODO change this to real fabricant id
    @property
    def fabricant_id(self):
        return self.fabricants


class RefVersion(models.Model):
    nom = models.CharField(max_length=255, unique=True, primary_key=True)

    def __str__(self):
        return self.nom


class Version(models.Model):
    # Fields
    app_label = "Version"
    code = models.CharField(max_length=20, primary_key=True)
    ref = models.ForeignKey(RefVersion, on_delete=models.CASCADE)
    images = models.ForeignKey(Image, on_delete=models.CASCADE)
    options = models.ManyToManyField('SayaraApi.Option', blank=True)
    modele = models.ForeignKey('SayaraApi.Modele', on_delete=models.CASCADE)
    prix_base = models.IntegerField()
    ficheTechnique = models.ForeignKey("SayaraApi.FicheTechnique", on_delete=models.CASCADE)
    couleur = models.ForeignKey("SayaraApi.Couleur", on_delete=models.CASCADE)

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
        query = TarifVersion.objects.filter(version=self, base=False, debut__lte=datetime.now(),
                                            fin__gte=datetime.now()).first()
        if query:
            return query.prix
        query = TarifVersion.objects.filter(base=True).last()
        if query:
            return query.prix
        return 0

    @property
    def nom(self):
        return self.ref.nom

    def __str__(self):
        return self.ref.nom


class RefModele(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Modele(models.Model):
    # Fields
    app_label = "Modele"
    code = models.CharField(max_length=10)
    ref = models.ForeignKey(RefModele, related_name="modele", on_delete=models.CASCADE)
    image = models.ImageField(default='images/vehicules/voiture.jpg', upload_to="images/vehicules")

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

    @classmethod
    def create(cls, new_ref):
        book = cls()
        # do something with the book
        return book


class Annonce(models.Model):
    # Fields
    app_label = "Annonce"
    # idAnnonce = models.AutoField(primary_key=True)

    titre = models.CharField(max_length=50)
    prix = models.IntegerField()
    commentaires = models.CharField(max_length=255)

    # Relationship Fields
    vehicule = models.ForeignKey('SayaraApi.VehiculeOccasion', on_delete="DO_NOTHING", )
    user = models.ForeignKey(User, related_name="proprietaire", on_delete="DO_NOTHING")

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


class Fabricant(models.Model):
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


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    is_fabricant = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    fabricant = models.ForeignKey(
        'SayaraApi.fabricant',
        on_delete=models.CASCADE, related_name="fabricant", blank=True, null=True
    )

    def __str__(self):
        return self.fabricant.nom


class RefCouleur(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom


class Couleur(models.Model):
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
        query = TarifCouleur.objects.filter(couleur=self, base=False, debut__lte=datetime.now(),
                                            fin__gte=datetime.now()).first()
        if query:
            return query.prix
        query = TarifOption.objects.filter(base=True).last()
        if query:
            return query.prix
        return 0


class RefOption(models.Model):
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom


class Option(models.Model):
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
        query = TarifOption.objects.filter(option=self, base=False, debut__lte=datetime.now(),
                                           fin__gte=datetime.now()).first()
        if query:
            return query.prix
        query = TarifOption.objects.filter(base=True).last()
        if query:
            return query.prix
        return 0

    @property
    def nom(self):
        return self.ref.nom


class VehiculeOccasion(Vehicule):
    kilometrage = models.IntegerField()
    date = models.DateField()
    image1 = models.ImageField(upload_to="images/vehicules", default='images/vehicules/voiture.jpg')
    image2 = models.ImageField(upload_to="images/vehicules", default='images/vehicules/voiture.jpg')
    image3 = models.ImageField(upload_to="images/vehicules", default='images/vehicules/voiture.jpg')
    version = models.ForeignKey(RefVersion, related_name="Refversion", on_delete="DO_NOTHING")
    model = models.ForeignKey(RefModele, related_name="model", on_delete="DO_NOTHING")
    options = models.ManyToManyField(RefOption, related_name="options", blank=True)


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
        return self.version.modele.marque

    @property
    def fabricant_id(self):
        return 1

    @property
    def fabricant_name(self):
        return "Notfixedyet"

    @property
    def image1(self):
        return self.version.images

    @property
    def modele_name(self):
        return self.version.modele_name

    @property
    def titre(self):
        return str(self.modele_name + " " + self.version.nom.nom)


class TarifOption(models.Model):
    debut = models.DateField()
    fin = models.DateField()
    prix = models.FloatField()
    base = models.BooleanField(default=False)
    # Relationship Fields
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="lignetarifs")

    @property
    def valid(self):
        return self.debut <= datetime.now() <= self.fin

    def __str__(self):
        return self.option.nom

    class Meta:
        ordering = ('-fin',)


class TarifVersion(models.Model):
    debut = models.DateField()
    fin = models.DateField()
    prix = models.FloatField()
    base = models.BooleanField(default=False)
    # Relationship Fields
    version = models.ForeignKey(Version, on_delete=models.CASCADE, related_name="lignetarifs")

    @property
    def valid(self):
        return self.debut <= datetime.now() < self.fin

    class Meta:
        ordering = ('-fin', 'version',)


class TarifCouleur(models.Model):
    debut = models.DateField()
    fin = models.DateField()
    prix = models.FloatField()
    base = models.BooleanField(default=False)
    # Relationship Fields
    couleur = models.ForeignKey(Couleur, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def valid(self):
        return self.debut <= datetime.now() < self.fin

    class Meta:
        ordering = ('-fin', 'couleur',)


class LigneTarif(models.Model):
    # Fields
    dateDebut = models.DateField()
    dateFin = models.DateField()
    prix = models.FloatField()


class FicheTechnique(models.Model):
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
