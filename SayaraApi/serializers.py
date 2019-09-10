from rest_framework import serializers

from SayaraApi.models import RefModele
from . import models
from .models import *


class CouleurSerializer(serializers.ModelSerializer):
    prix = serializers.IntegerField()

    class Meta:
        model = Couleur
        fields = (
            'pk',
            'code',
            'nom',
            'modele',
            'fabricantCouleur_id',
            'prix'
        )


class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculeNeuf
        fields = (
            'num',
            'disponible',
            'versionVoiture'
        )


class FabricantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricant
        fields = (
            'nom',
            'pk',
            'marque'
        )


class VehiculeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = (
            'disponible',
            'versionVoiture'
        )


class MarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marque
        fields = (
            'pk',
            'nom',
            'image',
        )


class OptionSerializer(serializers.ModelSerializer):
    prix = serializers.IntegerField()
    nom = serializers.CharField()

    class Meta:
        model = Option
        exclude = ("date_created", "date_modified", "date_removed",)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ("date_created", "date_modified", "date_removed",)


class VersionSerializer(serializers.ModelSerializer):
    nom = serializers.CharField()
    marque_name = serializers.CharField()
    prix = serializers.IntegerField()
    couleur = CouleurSerializer(many=True)
    options = OptionSerializer(many=True)
    ref_id = models.CharField()

    class Meta:
        model = Version
        exclude = ("date_created", "date_modified", "date_removed",)


class VersionDetailSerializer(serializers.ModelSerializer):
    nom = serializers.CharField()
    marque_name = serializers.CharField()
    prix = serializers.IntegerField()
    couleur = CouleurSerializer(many=True)
    options = OptionSerializer(many=True)
    ref_id = models.CharField()

    class Meta:
        model = Version
        exclude = ("date_created", "date_modified", "date_removed",)


class VersionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = (
            'ref',
            'code',
            'modele',
            'options',
            'images',
            'ficheTechnique'
        )


class ModeleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modele
        fields = ('__all__')


class ModeleByMarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modele
        fields = (
            'nom',
            'pk',
            'code',
            'fabricantModele',
        )


class ModeleCreateSerializer(serializers.ModelSerializer):
    new_ref = serializers.CharField(required=False, allow_blank=True,
                                    max_length=100)

    class Meta:
        model = Modele
        fields = ("new_ref", "code",)

    def create(self, validated_data):
        print(validated_data)
        new_ref = validated_data.get("new_ref", None)
        if new_ref is not None:
            try:
                marque = self.context['request'].user.profile.fabricant.marque
            except Exception as e:
                print("error", e)
                return validated_data
            if not marque:
                return validated_data
            try:
                new_ref = RefModele.objects.create(nom=new_ref, marque=marque)
            except:
                return validated_data
            validated_data["ref"] = new_ref
            validated_data.pop("new_ref")
        return Modele.objects.create(**validated_data)


class RefModeleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefModele
        fields = ('__all__')


class RefCouleurCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCouleur
        fields = ('__all__')


class RefCouleurCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCouleur
        fields = ('__all__')


class RefVersionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefVersion
        fields = ('__all__')


class OptionSerializer(serializers.ModelSerializer):
    prix = serializers.IntegerField()
    nom = serializers.CharField()

    class Meta:
        model = Option
        fields = ("__all__")


class OptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ("__all__")


class VehiculeOccasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculeOccasion
        exclude = (
            "date_created", "date_modified", "date_removed", "modele",
            "version")


class VehiculeOccasionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculeOccasion
        exclude = ("date_created", "date_modified", "date_removed",)


class VehiculeOccasionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculeOccasion
        exclude = (
            "date_created", "date_modified", "date_removed", "modele",
            "version")


class AnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annonce
        depth = 1
        exclude = ("modele", "version", "date")


class AnnonceUpdateSerializer(serializers.ModelSerializer):
    vehicule = VehiculeOccasionUpdateSerializer()

    class Meta:
        model = Annonce
        depth = 0
        exclude = ("user", "date_created", "date_modified", "date_removed")


class AnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annonce


class AnnonceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annonce
        exclude = ("user", "date_created", "date_modified", "date_removed",)

    def create(self, validated_data):
        validated_data["user"] = self.context['request'].user
        return Annonce.objects.create(**validated_data)


class AnnnonceNeufSerializer(serializers.ModelSerializer):
    fabricant_name = serializers.CharField()
    fabricant_id = serializers.IntegerField()
    marque = serializers.CharField()
    modele_name = serializers.CharField()
    image1 = serializers.ImageField()
    titre = serializers.CharField()

    class Meta:
        model = VehiculeNeuf
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
    marque_name = serializers.CharField()
    modele_name = serializers.CharField()
    version_name = serializers.CharField()
    couleur = serializers.CharField()

    class Meta:
        model = Annonce
        fields = "__all__"


class ModeleSerializer(serializers.ModelSerializer):
    couleur_set = CouleurSerializer(many=True, read_only=True, )

    class Meta:
        depth = 1
        model = Modele
        fields = (
            'nom',
            'pk',
            'code',
            'couleur_set',
            'image',
            'ref_id'
        )


class ModeleSerializerMobile(serializers.ModelSerializer):
    couleur_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Modele
        fields = (
            'nom',
            'pk',
            'code',
            'couleur_set',
            'image',
        )


class RefModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefModele
        fields = (
            '__all__'
        )


class RefCouleurSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCouleur
        fields = (
            '__all__'
        )


class RefVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefVersion
        fields = (
            '__all__'
        )


class LigneTarifSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneTarif
        fields = (
            '__all__'
        )


class TarifOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarifOption
        fields = (
            '__all__'
        )


class TarifCouleurSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarifCouleur
        fields = (
            '__all__'
        )


class TarifVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarifVersion
        fields = (
            '__all__'
        )


class FicheTechniqueSerializer(serializers.ModelSerializer):
    version_fiche = serializers.CharField()

    class Meta:
        model = FicheTechnique
        fields = (
            'pk',
            'nombrePortes',
            'boiteVitesse',
            'puissanceFiscale',
            'motorisation',
            'consommation',
            'dimensions',
            'transmission',
            'version_fiche',
            'capaciteReservoir',
            'vitesseMaxi',
            'acceleration',
            #            'images'
        )


class FicheTechniqueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FicheTechnique
        fields = (
            'pk',
            'nombrePortes',
            'boiteVitesse',
            'puissanceFiscale',
            'motorisation',
            'consommation',
            'dimensions',
            'transmission',
            'capaciteReservoir',
            'vitesseMaxi',
            'acceleration',
            #            'images'
        )


class FicheTechniqueViewAllSerializer(serializers.ModelSerializer):
    version_fiche = serializers.CharField()

    class Meta:
        model = FicheTechnique
        fields = (
            'pk',
            'nombrePortes',
            'boiteVitesse',
            'puissanceFiscale',
            'motorisation',
            'consommation',
            'dimensions',
            'transmission',
            'version_fiche',
            'capaciteReservoir',
            'vitesseMaxi',
            'acceleration',
            #            'images'
        )
        depth = 4


class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ("__all__")


class CommandeViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ("__all__")
        depth = 1


class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = (
            'annonce',
            'user',
            'prix',
        )


class VehiculeNeufSerializer(serializers.ModelSerializer):
    modele_name = serializers.CharField()
    fabricant_name = serializers.CharField()
    version = VersionSerializer()
    modele = ModeleSerializer()
    marque = serializers.CharField()
    options = OptionSerializer(many=True)

    class Meta:
        model = VehiculeNeuf
        fields = ("__all__")
