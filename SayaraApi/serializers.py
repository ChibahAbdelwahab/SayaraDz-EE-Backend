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
    modele_name = models.Modele
    marque_name = serializers.CharField()
    class Meta:
        model = models.Version
        fields = (
            'nomVersion',
            'codeVersion',
            "modele_name",
            'modeleVersion',
            'marque_name',
            'optionsVersion',
            'imagesVersion',
            'pk'
        )

class VersionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Version
        fields = (
            'nomVersion',
            'modeleVersion',
            'optionsVersion',
            'imagesVersion',
            'pk'
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
            'modeleOption'
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
    # titre = serializers.CharField()
    # idVehicule= VehiculeOccasionSerializer()
    pseudoUser = serializers.CharField()
    date = serializers.DateField()
    image1 = serializers.ImageField()
    image2 = serializers.ImageField()
    image3 = serializers.ImageField()
    kilometrage = serializers.IntegerField()

    class Meta:
        model = models.Annonce
        fields = "__all__"


class ModeleSerializer(serializers.ModelSerializer):
    # TODO remove idModele from nested couleur objects
    couleur_set = CouleurSerializer(many=True, read_only=True, )

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


class LigneTarifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LigneTarif
        fields = (
            'dateDebut',
            'dateFin',
            'prix',
            'code1',
            'code2',
            'code3'
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
            'consommation',
            'dimensions',
            'transmission',
            'idVersion'
        )