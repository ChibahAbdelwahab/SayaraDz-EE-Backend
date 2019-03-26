from . import models

from rest_framework import serializers


class VehiculeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Vehicule
        fields = (
            'numChassis',
            'disponible',
            'versionVoiture'
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
            'optionsVersion',
            'id2',
        )


class VersionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Version
        fields = (
            'nomVersion', 
            'codeVersion', 
            'modeleVersion',
            'optionsVersion'
        )


class ModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modele
        fields = ( 
            'nomModele', 
            'idModele', 
            'codeModele',
            'marqueModele',
            'couleurCompatible'
        )


class ModeleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modele
        fields = ( 
            'nomModele',
            'codeModele', 
            'marqueModele',
            'couleurCompatible'
        )


class ModeleByMarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modele
        fields = (
            'nomModele',
            'idModele', 
            'codeModele', 
            'marqueModele',
            'couleurCompatible'
        )


class FabricantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fabricant
        fields = (
            'nomFabricant',
            'idFabricant',
        )
class CouleurSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Couleur
        fields = (
            'codeCouleur',
            'nomCouleur',
        )

class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Option
        fields = (
            'nomOption',
            'codeOption',
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