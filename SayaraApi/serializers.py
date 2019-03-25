from . import models

from rest_framework import serializers


class VehiculeOccasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VehiculeOccasion
        fields = (
            'numChassis',
            'disponible',
            'versionVoiture',
            'kilometrage',
            'date'
        )

class VehiculeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicule
        fields = (
            'disponible',
            'versionVoiture'
        )


class MarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marque
        fields = (
            'idMarque',
            'nomMarque',
            'imageMarque',
        )


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Version
        fields = (
            'nomVersion',
            'codeVersion',
            'modeleVersion',
        )


class VersionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Version
        fields = (
            'nomVersion',
            'modeleVersion',
        )


class ModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modele
        fields = (
            'nomModele',
            'idModele',
            'marqueModele'
        )


class ModeleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modele
        fields = (
            'nomModele',
            'marqueModele'
        )


class ModeleByMarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modele
        fields = (
            'nomModele',
            'idModele',
            'marqueModele',
        )


class FabricantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fabricant
        fields = (
            'nomFabricant',
            'idFabricant',
        )


class AnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Annonce
        depth = 1
        exclude = ()

class VehiculeOccasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VehiculeOccasion
        fields = (
            'numChassis',
            'versionVoiture',
            'kilometrage',
            'date',
            'imageVehicle',
        )
class VehiculeNeufSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VehiculeNeuf
        fields = (
            'numChassis',
            'versionVoiture',
            'disponible',
            'prix'
        )

class AnnonceOccasionSerializer(serializers.ModelSerializer):
    titre = serializers.CharField()
    #idVehicule= VehiculeOccasionSerializer()
    idUser = serializers.StringRelatedField()
    date = serializers.DateField(source='idVehicule.date')
    imageVehicle=serializers.ImageField(source='idVehicule.imageVehicle')
    kilometrage = serializers.IntegerField(source='idVehicule.kilometrage')
    class Meta:
        model = models.Annonce
        fields="__all__"