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