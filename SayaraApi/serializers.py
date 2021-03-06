from rest_framework import serializers
from rest_framework.response import Response

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


class CouleurCreateSerializer(serializers.ModelSerializer):
    # prix = serializers.IntegerField()
    nom = serializers.CharField()

    class Meta:
        model = Couleur
        exclude = ("date_created", "date_modified", "date_removed", "ref")

    def create(self, validated_data):
        new_ref = validated_data.get("nom", None)
        new_ref, res = RefCouleur.objects.get_or_create(nom=new_ref)
        validated_data["ref"] = new_ref
        validated_data.pop("nom")
        print(validated_data)
        return Couleur.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance)
        print(RefCouleur.objects.filter(
            pk=Couleur.objects.get(ref__nom=instance).ref_id))
        instance.code = validated_data.get("code", instance.code)
        new_ref = validated_data.get("nom", None)
        if new_ref is not None:
            try:
                RefCouleur.objects.filter(
                    pk=Couleur.objects.get(ref__nom=instance).ref_id).update(
                    nom=new_ref)
            except:
                return validated_data
            validated_data.pop("nom")
            instance.save()
        return instance


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
    modele_name = serializers.CharField()
    marque_name = serializers.CharField()
    marque_id = serializers.CharField()
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
            'image1',
        )



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
    nom = serializers.CharField()

    class Meta:
        model = Option
        exclude = ("date_created", "date_modified", "date_removed", "ref")

    def create(self, validated_data):
        new_ref = validated_data.get("nom", None)
        new_ref, res = RefOption.objects.get_or_create(nom=new_ref)
        validated_data["ref"] = new_ref
        validated_data.pop("nom")
        return Option.objects.create(**validated_data)


class OptionUpdateSerializer(serializers.ModelSerializer):
    nom = serializers.CharField()

    class Meta:
        model = Option
        exclude = (
            "date_created", "date_modified", "date_removed", "ref", "code")

    def update(self, instance, validated_data):
        print(instance)
        print(RefOption.objects.filter(
            pk=Option.objects.get(ref__nom=instance).ref_id))
        new_ref = validated_data.get("nom", None)
        if new_ref is not None:
            try:
                RefOption.objects.filter(
                    pk=Option.objects.get(ref__nom=instance).ref_id).update(
                    nom=new_ref)
            except:
                return validated_data
            validated_data.pop("nom")
            instance.save()
        return instance


class VehiculeOccasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculeOccasion
        exclude = (
            "date_created", "date_modified", "date_removed",)


class VehiculeOccasionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculeOccasion
        exclude = ("date_created", "date_modified", "date_removed", "options")


class VehiculeOccasionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculeOccasion
        exclude = (
            "date_created", "date_modified", "date_removed", "modele",
            "options", "version")


class AnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annonce
        depth = 1
        exclude = ("modele", "version", "date")


class AnnonceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Annonce
        exclude = (
            "date_created", "date_modified", "date_removed", 'user', 'vehicule')


class AnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annonce


class AnnonceCreateSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # user = serializers.PrimaryKeyRelatedField(read_only=True,
    #                                           default=serializers.CurrentUserDefault())
    # Create a custom method field
    # user = serializers.SerializerMethodField('_user')

    # Use this method for the custom field
    # def _user(self, obj):
    #     request = getattr(self.context, 'request', None)
    #     if request:
    #         return request.user

    class Meta:
        model = Annonce
        exclude = ("date_created", "date_modified", "date_removed", "user")

    def create(self, validated_data):
        print(validated_data)
        try:
            validated_data["user"] = self.context['request'].user
            return Annonce.objects.create(**validated_data)
        except Exception as e:
            validated_data.pop("user")
            print(e)
        return Annonce.objects.create(**validated_data)


class AnnnonceNeufSerializer(serializers.ModelSerializer):
    fabricant_name = serializers.CharField()
    fabricant_id = serializers.IntegerField()
    marque = serializers.CharField()
    modele_name = serializers.CharField()
    image1 = serializers.ImageField()
    titre = serializers.CharField()
    version_id = serializers.CharField()

    class Meta:
        model = VehiculeNeuf
        fields = "__all__"


class VehiculeNeufSerialiser(serializers.ModelSerializer):
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
    version_id = serializers.CharField()

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
    couleur = couleur_set
    marque_nom = serializers.CharField()
    marqueId = serializers.IntegerField()

    class Meta:
        model = Modele
        fields = (
            'nom',
            'pk',
            'code',
            'couleur_set',
            'couleur',
            'image',
            'ref_id',
            'marque_nom',
            'marqueId'
        )


class RefModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefModele
        fields = (
            '__all__'
        )


class ModeleUpdateSerializer(serializers.ModelSerializer):
    new_ref = serializers.CharField(required=False, allow_blank=True,
                                    max_length=100)

    class Meta:
        model = Modele
        fields = ("new_ref", "code")

    def update(self, instance, validated_data):
        print(RefModele.objects.filter(
            pk=Modele.objects.get(ref__nom=instance).ref_id))
        instance.code = validated_data.get("code", instance.ref.nom)
        new_ref = validated_data.get("new_ref", None)
        if new_ref is not None:
            try:
                RefModele.objects.filter(
                    pk=Modele.objects.get(ref__nom=instance).ref_id).update(
                    nom=new_ref)
            except:
                return validated_data
            validated_data.pop("new_ref")
            instance.save()
        return instance


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
        exclude = ("date_created", "date_modified", "date_removed")


class CommandeListSerializer(serializers.ModelSerializer):
    vehicule = VehiculeNeufSerialiser()
    options = OptionSerializer(many=True)
    version = VersionSerializer()
    couleur = CouleurSerializer()

    class Meta:
        model = Commande
        exclude = ("date_created", "date_modified", "date_removed")


class CommandeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        exclude = (
            "date_created", "date_modified", "date_removed", "vehicule",
            "confirmation")


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


class OffreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = (
            'annonce', "prix"
        )

    def create(self, validated_data):
        try:
            validated_data["user"] = self.context['request'].user
            return Offre.objects.create(**validated_data)
        except Exception as e:
            validated_data.pop("user")
            print(e)
        return Offre.objects.create(**validated_data)


class VehiculeNeufSerializer(serializers.ModelSerializer):
    modele_name = serializers.CharField()
    fabricant_name = serializers.CharField()
    version = VersionSerializer()
    modele = ModeleSerializer()
    marque = serializers.CharField()
    options = OptionSerializer(many=True)
    couleur = CouleurSerializer()

    class Meta:
        model = VehiculeNeuf
        fields = ("__all__")


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)


class ProfileSerializer(serializers.ModelSerializer):
    user = UserListSerializer()

    class Meta:
        model = Profile
        exclude = ("date_created", "date_modified", "date_removed")


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class ProfileCreateSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()

    class Meta:
        model = Profile
        exclude = ("date_created", "date_modified", "date_removed")
