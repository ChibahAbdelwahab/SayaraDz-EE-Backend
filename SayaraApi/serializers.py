from rest_framework import serializers

from . import models


class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicule
        fields = (
            'num',
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
            'nom',
            'image',
        )


class VersionSerializer(serializers.ModelSerializer):
    modele_name = models.Modele
    marque_name = serializers.CharField()

    class Meta:
        model = models.Version
        fields = (
            'nom',
            'code',
            "modele_name",
            'modele',
            'marque_name',
            'options',
            'images',
            'pk'
        )


class VersionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Version
        fields = (
            'nom',
            'code',
            'modele',
            'options',
            'images',
            'pk'
        )


class ModeleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modele
        fields = (
            '__all__'
        )


class ModeleByMarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modele
        fields = (
            'nom',
            'pk',
            'code',
            'fabricantModele',
            # 'couleurCompatible'
        )


class fabricantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.fabricant
        fields = (
            'nom',
            'pk',
            'marque'
        )


class CouleurSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Couleur
        fields = (
            'pk',
            'code',
            'nom',
            'modele',
            'fabricantCouleur_id'
        )


class ModeleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modele
        fields = ('__all__')


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Option
        fields = (
            'nom',
            'code',
            'modele'
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
            'num',
            'versionVoiture',
            'kilometrage',
            'date',
            'imageVehicle',
        )


class VehiculeNeufSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VehiculeNeuf
        fields = (
            'num',
            'version',
            'disponible',
            'prix',

        )


class AnnnonceNeufSerializer(serializers.ModelSerializer):
    fabricant_name = serializers.CharField()
    fabricant_id = serializers.IntegerField()
    marque = serializers.CharField()
    modele_name = serializers.CharField()
    image1 = serializers.ImageField()
    titre = serializers.CharField()

    class Meta:
        model = models.VehiculeNeuf
        fields = "__all__"


class AnnonceOccasionSerializer(serializers.ModelSerializer):
    # titre = serializers.CharField()
    # vehicule= VehiculeOccasionSerializer()
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
    couleur_set = CouleurSerializer(many=True, read_only=True, )

    class Meta:
        depth = 1
        model = models.Modele
        fields = (
            'nom',
            'pk',
            'marque',
            'code',
            'couleur_set',
            'nom',
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
            'version',
            'capaciteReservoir',
            'vitesseMaxi',
            'acceleration',
            'images'
        )


class FicheTechniqueViewAllSerializer(serializers.ModelSerializer):
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
            'version',
            'capaciteReservoir',
            'vitesseMaxi',
            'acceleration',
            'images'
        )

        depth = 4
