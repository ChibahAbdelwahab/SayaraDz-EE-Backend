from django.contrib.auth.models import User
from django.db import models as models
from django.urls import reverse


class Vehicule(models.Model):
    # Fields
    app_label = "Vehicule"
    numChassis = models.CharField(max_length=100)
    idVehicule = models.AutoField(primary_key=True)
    imageVehicle1 = models.ImageField(upload_to="images/vehicules", default='images/vehicules/voiture.jpg')
    imageVehicle2 = models.ImageField(upload_to="images/vehicules", null=True, blank=True)
    imageVehicle3 = models.ImageField(upload_to="images/vehicules", null=True, blank=True)

    # Relationship Fields
    versionVoiture = models.ForeignKey(
        'SayaraApi.Version',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-pk',)
        abstract = True

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('SayaraApi_vehicule_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('SayaraApi_vehicule_update', args=(self.pk,))

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
        on_delete=models.CASCADE, related_name="versions",
    )

    @property
    def fabricantVersion_id(self):
        return self.modeleVersion.fabricantModele_id

    def __str__(self):
        return self.nomVersion


class Modele(models.Model):
    # Fields
    app_label = "Modele"
    codeModele = models.CharField(max_length=10)
    nomModele = models.CharField(max_length=255)
    fabricantModele = models.ForeignKey(
        'SayaraApi.fabricant', on_delete=models.CASCADE, )

    def __str__(self):
        return self.nomModele


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


class Couleur(models.Model):
    app_label = "Couleur"
    codeCouleur = models.CharField(max_length=3)
    nomCouleur = models.CharField(max_length=50)

    ModeleCouleur = models.ForeignKey(
        'SayaraApi.Modele',
        on_delete=models.CASCADE, blank=False, null=False
    )

    def __str__(self):
        return self.nomCouleur

    @property
    def fabricantCouleur_id(self):
        return self.ModeleCouleur.fabricantModele_id
    # class Meta:
    #     permissions = (
    #         ('can_change_post_name', "Can change post name"),
    #     )
    #
    # def can_change_name(self, user):
    #     return self.user == user or user.is_staff
    #
    # def can_change_content(self, user):
    #     return self.user == user or user.is_staff


class Option(models.Model):
    # Fields
    nomOption = models.CharField(max_length=255)
    codeOption = models.CharField(max_length=100, primary_key=True)
    fabricantOption_id = models.ForeignKey(
        'SayaraApi.Fabricant',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,

    )

    def save(self,fabricantOption_id=None, *args, **kwargs):
        print(fabricantOption_id,args,kwargs)
        # if not self.pk:
        #     self.fabricantOption_id=Fabricant.objects.get(pk=1)
        super(Option, self).save(*args, **kwargs)
   
        
    def __str__(self):
        return self.nomOption


class VehiculeOccasion(Vehicule):
    kilometrage = models.IntegerField()
    date = models.DateField()


class VehiculeNeuf(Vehicule):
    disponible = models.BooleanField()
    fabricantVehicule = models.ForeignKey(
        'SayaraApi.Fabricant',
        on_delete=models.CASCADE,
    )

    @property
    def prix(self):
        return 122
