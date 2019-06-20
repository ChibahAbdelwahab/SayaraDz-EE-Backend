from django.contrib.auth.models import User
from django.db import models as models


class Vehicule(models.Model):
    # Fields
    app_label = "Vehicule"
    numChassis = models.CharField(max_length=100)
    idVehicule = models.AutoField(primary_key=True)

    @property
    def marque(self):
        return self.versionVoiture.modeleVersion.nomModele.marqueModele

    @property
    def version(self):
        return self.versionVoiture.nomVersion

    @property
    def modele_name(self):
        return self.versionVoiture.modeleVersion.nomModele

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
        return self.nomMarque


class RefVersion(models.Model):
    nomVersion = models.CharField(max_length=255, unique=True, primary_key=True)

    def __str__(self):
        return self.nomVersion


class Version(models.Model):
    # Fields
    app_label = "Version"
    codeVersion = models.CharField(max_length=20)
    nomVersion = models.ForeignKey(RefVersion, on_delete=models.CASCADE)
    imagesVersion = models.ImageField(upload_to="images/versions", null=True, blank=True)
    # Relationship Fields
    optionsVersion = models.ManyToManyField(
        'SayaraApi.Option',
        related_name="versions",
        blank=True
    )


    modeleVersion = models.ForeignKey(
        'SayaraApi.Modele',
        on_delete=models.CASCADE, related_name="versions"
    )

    @property
    def fabricantVersion_id(self):
        return self.modeleVersion.nomModele.marqueModele

    @property
    def modele_name(self):
        return self.modeleVersion.nomModele.nomModele

    @property
    def marque_name(self):
        return self.modeleVersion.nomModele.marqueModele.nomMarque

    def __str__(self):
        return self.nomVersion.nomVersion


class Image(models.Model):
    image = models.ImageField(upload_to="images/vehicules", null=True, blank=True)


class RefModele(models.Model):
    nomModele = models.CharField(max_length=255, unique=True)
    marqueModele = models.ForeignKey(Marque, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomModele


class Modele(models.Model):
    # Fields
    app_label = "Modele"
    codeModele = models.CharField(max_length=10)
    nomModele = models.ForeignKey(RefModele, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomModele.nomModele

    @property
    def nom(self):
        return self.nomModele.nomModele

    @property
    def marque(self):
        return self.nomModele.marqueModele.nomMarque


class Annonce(models.Model):
    # Fields
    app_label = "Annonce"
    # idAnnonce = models.AutoField(primary_key=True)

    titre = models.CharField(max_length=50)
    prix = models.IntegerField()
    commentaires = models.CharField(max_length=255)

    # Relationship Fields
    idVehicule = models.ForeignKey(
        'SayaraApi.VehiculeOccasion',
        related_name="vehicule",
        on_delete="DO_NOTHING",
    )
    idUser = models.ForeignKey(
        User,
        related_name="proprietaire",
        on_delete="DO_NOTHING",
    )

    @property
    def image1(self):
        return self.idVehicule.image1

    @property
    def image2(self):
        return self.idVehicule.image2

    @property
    def image3(self):
        return self.idVehicule.image3

    @property
    def kilometrage(self):
        return self.idVehicule.kilometrage

    @property
    def pseudoUser(self):
        return self.idUser.username

    @property
    def date(self):
        return self.idVehicule.date

    def __str__(self):
        return self.titre


class Fabricant(models.Model):
    app_label = "Fabricant"
    # Fields
    nomFabricant = models.CharField(max_length=255)

    # Relationship Fields
    marqueFabricant = models.ForeignKey(
        'SayaraApi.Marque',
        on_delete=models.CASCADE, related_name="fabricants",
    )

    def __str__(self):
        return self.nomFabricant


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    is_fabricant = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    Fabricant = models.ForeignKey(
        'SayaraApi.fabricant',
        on_delete=models.CASCADE, related_name="fabricant", blank=True, null=True
    )

    def __str__(self):
        return Fabricant.nomFabricant


class RefCouleur(models.Model):
    nomCouleur = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nomCouleur


class Couleur(models.Model):
    app_label = "Couleur"
    codeCouleur = models.CharField(max_length=3)
    nomCouleur = models.ForeignKey(RefCouleur, on_delete=models.CASCADE)

    ModeleCouleur = models.ForeignKey(
        'SayaraApi.Modele',
        on_delete=models.CASCADE, blank=False, null=False
    )

    def __str__(self):
        return self.nomCouleur.nomCouleur

    @property
    def fabricantCouleur_id(self):
        return self.ModeleCouleur.fabricantModele_id


class RefOption(models.Model):
    nomOption = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nomOption


class Option(models.Model):
    # Fields
    nomOption = models.ForeignKey(RefOption, on_delete=models.CASCADE)
    codeOption = models.CharField(max_length=100, primary_key=True)
    modeleOption = models.ForeignKey('SayaraApi.modele', on_delete=models.CASCADE)

    # def save(self, fabricantOption_id=None, *args, **kwargs):
    #     print(fabricantOption_id, args, kwargs)
    #     # if not self.pk:
    #     #     self.fabricantOption_id=Fabricant.objects.get(pk=1)
    #     super(Option, self).save(*args, **kwargs)
    def __str__(self):
        return self.nomOption.nomOption


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
    optionsVersion = models.ManyToManyField(Option, blank=True)

    @property
    def prix(self):
        return 122


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
    idVersion = models.OneToOneField(Version,
                                  related_name="fichetechniques",
                                  on_delete="DO_NOTHING", )
    nombrePortes = models.CharField(max_length=100)
    boiteVitesse = models.CharField(max_length=100)
    puissanceFiscale = models.CharField(max_length=100)
    motorisation = models.CharField(max_length=100)
    consommation = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
