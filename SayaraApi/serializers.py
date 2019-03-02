from . import models

from rest_framework import serializers


class VehiculeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Vehicule
        fields = (
            'pk', 
            'numChassis', 
            'disponible', 
            'versionVoiture'
        )


class MarqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Marque
        fields = (
            'pk', 
            'idMarque', 
            'nomMarque',
            'imageMarque',

        )


class VersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Version
        fields = (
            'pk', 
            'nomVersion', 
            'codeVersion', 
            'modeleVersion',
        )


class ModeleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Modele
        fields = (
            'pk', 
            'nomModele', 
            'idModele', 
            'marqueModele',
        )

class ModeleByMarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modele
        fields = (
            'pk', 
            'nomModele', 
            'idModele', 
            'marqueModele',
        )

