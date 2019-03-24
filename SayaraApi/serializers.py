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
            'optionsVersion'
        )

class VersionUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Version
        fields = (
            'nomVersion', 
            'modeleVersion',
            'optionsVersion'
        )

class ModeleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Modele
        fields = ( 
            'nomModele', 
            'idModele', 
            'marqueModele',
            'couleurCompatible'
        )

    

class ModeleUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Modele
        fields = ( 
            'nomModele', 
            'marqueModele',
            'couleurCompatible'
        )

class ModeleByMarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modele
        fields = (
            'nomModele', 
            'idModele', 
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