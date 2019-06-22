from django.contrib.auth.models import User
from django.db import models as models


class Vehicule(models.Model):
    # Fields
    app_label = "Vehicule"
    numChassis = models.CharField(max_length=100)
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
        return self.numChassis


class Marque(models.Model):
    # Fields
    app_label = "Marque"
    nomMarque = models.CharField(max_length=50)
    imageMarque = models.ImageField(upload_to="marque/images/")

    def __str__(self):
        return self.nomMarque

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
    nom = models.ForeignKey(RefVersion, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="images/versions", null=True, blank=True)
    # Relationship Fields
    options = models.ManyToManyField(
        'SayaraApi.Option',
        related_name="versions",
        blank=True
    )

    modele = models.ForeignKey(
        'SayaraApi.Modele',
        on_delete=models.CASCADE, related_name="versions"
    )

    @property
    def fabricantVersion_id(self):
        return self.modele.nom.marque

    @property
    def modele_name(self):
        return self.modele.nom.nom

    @property
    def marque_name(self):
        return self.modele.nom.marque.nomMarque

    def __str__(self):
        return self.nom.nom


class Image(models.Model):
    image = models.ImageField(upload_to="images/vehicules", null=True, blank=True)


class RefModele(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Modele(models.Model):
    # Fields
    app_label = "Modele"
    code = models.CharField(max_length=10)
    nom = models.ForeignKey(RefModele, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom.nom

    @property
    def nom(self):
        return self.nom.nom

    @property
    def fabricant_name(self):
        return self.nom.marque.fabricant

    @property
    def fabricant_id(self):
        return self.nom.marque

    @property
    def marque(self):
        return self.nom.marque.nomMarque


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


class fabricant(models.Model):
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


#
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
        return fabricant.nom


class RefCouleur(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom


class Couleur(models.Model):
    app_label = "Couleur"
    code = models.CharField(max_length=3)
    nom = models.ForeignKey(RefCouleur, on_delete=models.CASCADE)

    modele = models.ForeignKey(
        'SayaraApi.Modele',
        on_delete=models.CASCADE, blank=False, null=False
    )

    def __str__(self):
        return self.nom.nom

    @property
    def fabricantCouleur_id(self):
        return self.modele.fabricantModele_id


class RefOption(models.Model):
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom


class Option(models.Model):
    # Fields
    nom = models.ForeignKey(RefOption, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, primary_key=True)
    modele = models.ForeignKey('SayaraApi.modele', on_delete=models.CASCADE)

    # def save(self, fabricantOption_id=None, *args, **kwargs):
    #     print(fabricantOption_id, args, kwargs)
    #     # if not self.pk:
    #     #     self.fabricantOption_id=fabricant.objects.get(pk=1)
    #     super(Option, self).save(*args, **kwargs)
    def __str__(self):
        return self.nom.nom


class VehiculeOccasion(Vehicule):
    kilometrage = models.IntegerField()
    date = models.DateField()
    image1 = models.ImageField(upload_to="images/vehicules", default='images/vehicules/voiture.jpg')
    image2 = models.ImageField(upload_to="images/vehicules", null=True, blank=True)
    image3 = models.ImageField(upload_to="images/vehicules", null=True, blank=True)
    version = models.ForeignKey(RefVersion, related_name="Refversion", on_delete="DO_NOTHING")
    model = models.ForeignKey(RefModele, related_name="model", on_delete="DO_NOTHING")
    options = models.ManyToManyField(RefOption, related_name="options", blank=True)


class VehiculeNeuf(Vehicule):
    disponible = models.BooleanField()
    concessionnaire = models.CharField(max_length=250)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)
    options = models.ManyToManyField(Option, blank=True)

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


class LigneTarif(models.Model):
    # Fields
    dateDebut = models.DateField()
    dateFin = models.DateField()
    prix = models.FloatField()

    # Relationship Fields
    code1 = models.OneToOneField(
        Version,
        on_delete=models.CASCADE, related_name="lignetarifs",
        blank=True, null=True
    )
    code2 = models.OneToOneField(
        Option,
        on_delete=models.CASCADE, related_name="lignetarifs",
        blank=True, null=True
    )
    code3 = models.OneToOneField(
        Couleur,
        on_delete=models.CASCADE, related_name="lignetarifs",
        blank=True, null=True
    )

    class Meta:
        ordering = ('-pk',)


class FicheTechnique(models.Model):
    version = models.OneToOneField(Version,
                                   related_name="fichetechniques",
                                   on_delete="DO_NOTHING", )
    nombrePortes = models.CharField(max_length=100)
    boiteVitesse = models.CharField(max_length=100)
    puissanceFiscale = models.CharField(max_length=100)
    motorisation = models.CharField(max_length=100)
    consommation = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    capaciteReservoir = models.CharField(max_length=100)
    vitesseMaxi = models.IntegerField()
    acceleration = models.CharField(max_length=100)
    images = models.ManyToManyField(
        Image,
        blank=True
    )
