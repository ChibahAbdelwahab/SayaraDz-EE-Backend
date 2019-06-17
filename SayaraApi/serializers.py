from rest_framework import serializers

from . import models


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
            'pk',
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
            'pk',
        )


class ModeleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modele
        fields = (
            'nomModele',
            'codeModele',
            'fabricantModele',
            # 'couleurCompatible'
        )


class ModeleByMarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modele
        fields = (
            'nomModele',
            'pk',
            'codeModele',
            'fabricantModele',
            # 'couleurCompatible'
        )


class FabricantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fabricant
        fields = (
            'nomFabricant',
            'pk',
            'marqueFabricant'
        )


class CouleurSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Couleur
        fields = (
            'pk',
            'codeCouleur',
            'nomCouleur',
            'ModeleCouleur',
            'fabricantCouleur_id'
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
    # idVehicule= VehiculeOccasionSerializer()
    idUser = serializers.StringRelatedField()
    date = serializers.DateField(source='idVehicule.date')
    imageVehicle1 = serializers.ImageField(source='idVehicule.imageVehicle1')
    imageVehicle2 = serializers.ImageField(source='idVehicule.imageVehicle2')
    imageVehicle3 = serializers.ImageField(source='idVehicule.imageVehicle3')
    kilometrage = serializers.IntegerField(source='idVehicule.kilometrage')

    class Meta:
        model = models.Annonce
        fields = "__all__"


class ModeleSerializer(serializers.ModelSerializer):
    #TODO remove idModele from nested couleur objects
    couleur_set = CouleurSerializer(many=True,read_only=True,)
    class Meta:
        depth = 1
        model = models.Modele
        fields = (
            'nom',
            'pk',
            'marque',
            'codeModele',
            'couleur_set',
        )

class FicheTechniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FicheTechnique
        fields = (
            'pk',
            'nombrePortes',
            'boiteVitesse',
            'puissanceFiscale',
            'motorisation',
            'consomation',
            'dimension',
            'transmission',
        )
