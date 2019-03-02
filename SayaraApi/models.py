from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import TextField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Vehicule(models.Model):
    # Fields
    app_label = "Vehicule"
    numChassis = models.CharField(max_length=100, primary_key=True)
    disponible = models.BooleanField()
    imageVehicle = models.ImageField(upload_to="images/vehicules",default='images/vehicules/voiture.jpg')

    # Relationship Fields
    versionVoiture = models.ForeignKey(
        'SayaraApi.Version',
        on_delete=models.CASCADE, related_name="vehicules",
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('SayaraApi_vehicule_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('SayaraApi_vehicule_update', args=(self.pk,))


class Marque(models.Model):
    # Fields
    app_label = "Marque"
    idMarque = models.AutoField(primary_key=True)
    nomMarque = models.CharField(max_length=50)
    imageMarque = models.ImageField(upload_to="images/marques")

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('SayaraApi_marque_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('SayaraApi_marque_update', args=(self.pk,))

    def __str__(self):
        return self.nomMarque


class Version(models.Model):
    # Fields
    app_label = "Version"
    nomVersion = models.CharField(max_length=100)
    codeVersion = models.CharField(max_length=20, primary_key=True)

    # Relationship Fields
    modeleVersion = models.ForeignKey(
        'SayaraApi.Modele',
        on_delete=models.CASCADE, related_name="versions",
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('SayaraApi_version_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('SayaraApi_version_update', args=(self.pk,))

    def __str__(self):
        return self.nomVersion


class Modele(models.Model):
    # Fields
    app_label = "Modele"
    nomModele = models.CharField(max_length=255)
    idModele = models.AutoField(primary_key=True)

    # Relationship Fields
    marqueModele = models.ForeignKey(
        'SayaraApi.Marque',
        on_delete=models.CASCADE, related_name="modeles",
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('SayaraApi_modele_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('SayaraApi_modele_update', args=(self.pk,))

    def __str__(self):
        return self.nomModele
