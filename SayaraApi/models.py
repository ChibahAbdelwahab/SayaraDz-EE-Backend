from django.contrib.auth.models import User
from django.db import models as models


class Vehicule(models.Model):
    # Fields
    app_label = "Vehicule"
    numChassis = models.CharField(max_length=100)
    idVehicule = models.AutoField(primary_key=True)

    # Relationship Fields
    versionVoiture = models.ForeignKey(
        'SayaraApi.Version',
        on_delete=models.CASCADE,
    )

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


class Version(models.Model):
    # Fields
    app_label = "Version"
    nomVersion = models.CharField(max_length=100)
    codeVersion = models.CharField(max_length=20)

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
        return self.modeleVersion.fabricantModele_id

    def __str__(self):
        return self.nomVersion


class RefModele(models.Model):
    nomModele = models.CharField(max_length=255)
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


class Annonce(models.Model):
    # Fields
    app_label = "Annonce"
    # idAnnonce = models.AutoField(primary_key=True)

    titre = models.CharField(max_length=50)
    prix = models.IntegerField()
    commentaites = models.CharField(max_length=255)

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

    def __str__(self):
        return self.titre


class Fabricant(models.Model):
    app_label = "Fabricant"
    # Fields
    nomFabricant = models.CharField(max_length=255)

    # Relationship Fields
    marqueFabricant = models.ForeignKey(
        'SayaraApi.marque',
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


class RefCouleur(models.Model):
    nomCouleur = models.CharField(max_length=50)
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
#

class RefOption(models.Model):
    nomOption = models.CharField(max_length=255)

    def __str__(self):
        return  self.nomOption


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
    imageVehicle1 = models.ImageField(upload_to="images/vehicules", default='images/vehicules/voiture.jpg')
    imageVehicle2 = models.ImageField(upload_to="images/vehicules", null=True, blank=True)
    imageVehicle3 = models.ImageField(upload_to="images/vehicules", null=True, blank=True)
    options = models.ManyToManyField(
        'SayaraApi.RefOption',
        related_name="options",
        blank=True
    )


class VehiculeNeuf(Vehicule):
    disponible = models.BooleanField()
    concessionnaire = models.CharField(max_length=250)

    optionsVersion = models.ManyToManyField(
        'SayaraApi.Option',
        blank=True
    )

    @property
    def prix(self):
        return 122
