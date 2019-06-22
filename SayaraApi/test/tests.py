import unittest
from django.urls import reverse
from django.test import Client
from .models import Vehicule, Marque, Version, Modele, Annonce, Fabricant, Profile, Couleur, Option, RefVersion, Image, RefModele, fabricant, RefCouleur, RefOption, LigneTarif, FicheTechnique
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_vehicule(**kwargs):
    defaults = {}
    defaults["num"] = "num"
    defaults["idVehicule"] = "idVehicule"
    defaults["imageVehicle1"] = "imageVehicle1"
    defaults["imageVehicle2"] = "imageVehicle2"
    defaults["imageVehicle3"] = "imageVehicle3"
    defaults.update(**kwargs)
    return Vehicule.objects.create(**defaults)


def create_marque(**kwargs):
    defaults = {}
    defaults["idMarque"] = "idMarque"
    defaults["nom"] = "nom"
    defaults["image"] = "image"
    defaults.update(**kwargs)
    return Marque.objects.create(**defaults)


def create_version(**kwargs):
    defaults = {}
    defaults["nomVersion"] = "nomVersion"
    defaults["codeVersion"] = "codeVersion"
    defaults.update(**kwargs)
    return Version.objects.create(**defaults)


def create_modele(**kwargs):
    defaults = {}
    defaults["idModele"] = "idModele"
    defaults["nomModele"] = "nomModele"
    defaults.update(**kwargs)
    if "couleurCompatible" not in defaults:
        defaults["couleurCompatible"] = create_"sayaraapi_couleur"()
    if "marqueModele" not in defaults:
        defaults["marqueModele"] = create_'sayaraapi_marque'()
    if "couleurCompatible" not in defaults:
        defaults["couleurCompatible"] = create_'sayaraapi_couleur'()
    return Modele.objects.create(**defaults)


def create_annonce(**kwargs):
    defaults = {}
    defaults["titre"] = "titre"
    defaults["prix"] = "prix"
    defaults["commentaites"] = "commentaites"
    defaults.update(**kwargs)
    return Annonce.objects.create(**defaults)


def create_fabricant(**kwargs):
    defaults = {}
    defaults["nomFabricant"] = "nomFabricant"
    defaults["idFabricant"] = "idFabricant"
    defaults.update(**kwargs)
    return Fabricant.objects.create(**defaults)


def create_profile(**kwargs):
    defaults = {}
    defaults["is_fabricant"] = "is_fabricant"
    defaults["is_client"] = "is_client"
    defaults.update(**kwargs)
    if "Fabricant" not in defaults:
        defaults["Fabricant"] = create_'sayaraapi_fabricant'()
    return Profile.objects.create(**defaults)


def create_couleur(**kwargs):
    defaults = {}
    defaults["codeCouleur"] = "codeCouleur"
    defaults["nomCouleur"] = "nomCouleur"
    defaults.update(**kwargs)
    return Couleur.objects.create(**defaults)


def create_option(**kwargs):
    defaults = {}
    defaults["nomOption"] = "nomOption"
    defaults["codeOption"] = "codeOption"
    defaults["kilometrage"] = "kilometrage"
    defaults["date"] = "date"
    defaults["disponible"] = "disponible"
    defaults.update(**kwargs)
    if "idFabricant" not in defaults:
        defaults["idFabricant"] = create_'sayaraapi_fabricant'()
    return Option.objects.create(**defaults)


def create_refversion(**kwargs):
    defaults = {}
    defaults["nom"] = "nom"
    defaults.update(**kwargs)
    return RefVersion.objects.create(**defaults)


def create_image(**kwargs):
    defaults = {}
    defaults["image"] = "image"
    defaults.update(**kwargs)
    return Image.objects.create(**defaults)


def create_refmodele(**kwargs):
    defaults = {}
    defaults["nom"] = "nom"
    defaults.update(**kwargs)
    if "marque" not in defaults:
        defaults["marque"] = create_marque()
    return RefModele.objects.create(**defaults)


def create_fabricant(**kwargs):
    defaults = {}
    defaults["nom"] = "nom"
    defaults.update(**kwargs)
    return fabricant.objects.create(**defaults)


def create_refcouleur(**kwargs):
    defaults = {}
    defaults["nom"] = "nom"
    defaults.update(**kwargs)
    return RefCouleur.objects.create(**defaults)


def create_refoption(**kwargs):
    defaults = {}
    defaults["nom"] = "nom"
    defaults.update(**kwargs)
    return RefOption.objects.create(**defaults)


def create_lignetarif(**kwargs):
    defaults = {}
    defaults["dateDebut"] = "dateDebut"
    defaults["dateFin"] = "dateFin"
    defaults["prix"] = "prix"
    defaults.update(**kwargs)
    return LigneTarif.objects.create(**defaults)


def create_fichetechnique(**kwargs):
    defaults = {}
    defaults["nombrePortes"] = "nombrePortes"
    defaults["boiteVitesse"] = "boiteVitesse"
    defaults["puissanceFiscale"] = "puissanceFiscale"
    defaults["motorisation"] = "motorisation"
    defaults["consommation"] = "consommation"
    defaults["dimensions"] = "dimensions"
    defaults["transmission"] = "transmission"
    defaults["capaciteReservoir"] = "capaciteReservoir"
    defaults["vitesseMaxi"] = "vitesseMaxi"
    defaults["acceleration"] = "acceleration"
    defaults.update(**kwargs)
    if "images" not in defaults:
        defaults["images"] = create_image()
    return FicheTechnique.objects.create(**defaults)


class VehiculeViewTest(unittest.TestCase):
    '''
    Tests for Vehicule
    '''
    def setUp(self):
        self.client = Client()

    def test_list_vehicule(self):
        url = reverse('SayaraApi_vehicule_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_vehicule(self):
        url = reverse('SayaraApi_vehicule_create')
        data = {
            "num": "num",
            "idVehicule": "idVehicule",
            "imageVehicle1": "imageVehicle1",
            "imageVehicle2": "imageVehicle2",
            "imageVehicle3": "imageVehicle3",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_vehicule(self):
        vehicule = create_vehicule()
        url = reverse('SayaraApi_vehicule_detail', args=[vehicule.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_vehicule(self):
        vehicule = create_vehicule()
        data = {
            "num": "num",
            "idVehicule": "idVehicule",
            "imageVehicle1": "imageVehicle1",
            "imageVehicle2": "imageVehicle2",
            "imageVehicle3": "imageVehicle3",
        }
        url = reverse('SayaraApi_vehicule_update', args=[vehicule.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class MarqueViewTest(unittest.TestCase):
    '''
    Tests for Marque
    '''
    def setUp(self):
        self.client = Client()

    def test_list_marque(self):
        url = reverse('SayaraApi_marque_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_marque(self):
        url = reverse('SayaraApi_marque_create')
        data = {
            "idMarque": "idMarque",
            "nom": "nom",
            "image": "image",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_marque(self):
        marque = create_marque()
        url = reverse('SayaraApi_marque_detail', args=[marque.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_marque(self):
        marque = create_marque()
        data = {
            "idMarque": "idMarque",
            "nom": "nom",
            "image": "image",
        }
        url = reverse('SayaraApi_marque_update', args=[marque.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class VersionViewTest(unittest.TestCase):
    '''
    Tests for Version
    '''
    def setUp(self):
        self.client = Client()

    def test_list_version(self):
        url = reverse('SayaraApi_version_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_version(self):
        url = reverse('SayaraApi_version_create')
        data = {
            "nomVersion": "nomVersion",
            "codeVersion": "codeVersion",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_version(self):
        version = create_version()
        url = reverse('SayaraApi_version_detail', args=[version.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_version(self):
        version = create_version()
        data = {
            "nomVersion": "nomVersion",
            "codeVersion": "codeVersion",
        }
        url = reverse('SayaraApi_version_update', args=[version.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ModeleViewTest(unittest.TestCase):
    '''
    Tests for Modele
    '''
    def setUp(self):
        self.client = Client()

    def test_list_modele(self):
        url = reverse('SayaraApi_modele_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_modele(self):
        url = reverse('SayaraApi_modele_create')
        data = {
            "idModele": "idModele",
            "nomModele": "nomModele",
            "couleurCompatible": create_"sayaraapi_couleur"().pk,
            "marqueModele": create_'sayaraapi_marque'().pk,
            "couleurCompatible": create_'sayaraapi_couleur'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_modele(self):
        modele = create_modele()
        url = reverse('SayaraApi_modele_detail', args=[modele.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_modele(self):
        modele = create_modele()
        data = {
            "idModele": "idModele",
            "nomModele": "nomModele",
            "couleurCompatible": create_"sayaraapi_couleur"().pk,
            "marqueModele": create_'sayaraapi_marque'().pk,
            "couleurCompatible": create_'sayaraapi_couleur'().pk,
        }
        url = reverse('SayaraApi_modele_update', args=[modele.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AnnonceViewTest(unittest.TestCase):
    '''
    Tests for Annonce
    '''
    def setUp(self):
        self.client = Client()

    def test_list_annonce(self):
        url = reverse('SayaraApi_annonce_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_annonce(self):
        url = reverse('SayaraApi_annonce_create')
        data = {
            "titre": "titre",
            "prix": "prix",
            "commentaites": "commentaites",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_annonce(self):
        annonce = create_annonce()
        url = reverse('SayaraApi_annonce_detail', args=[annonce.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_annonce(self):
        annonce = create_annonce()
        data = {
            "titre": "titre",
            "prix": "prix",
            "commentaites": "commentaites",
        }
        url = reverse('SayaraApi_annonce_update', args=[annonce.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class FabricantViewTest(unittest.TestCase):
    '''
    Tests for Fabricant
    '''
    def setUp(self):
        self.client = Client()

    def test_list_fabricant(self):
        url = reverse('SayaraApi_fabricant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_fabricant(self):
        url = reverse('SayaraApi_fabricant_create')
        data = {
            "nomFabricant": "nomFabricant",
            "idFabricant": "idFabricant",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_fabricant(self):
        fabricant = create_fabricant()
        url = reverse('SayaraApi_fabricant_detail', args=[fabricant.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_fabricant(self):
        fabricant = create_fabricant()
        data = {
            "nomFabricant": "nomFabricant",
            "idFabricant": "idFabricant",
        }
        url = reverse('SayaraApi_fabricant_update', args=[fabricant.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProfileViewTest(unittest.TestCase):
    '''
    Tests for Profile
    '''
    def setUp(self):
        self.client = Client()

    def test_list_profile(self):
        url = reverse('SayaraApi_profile_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_profile(self):
        url = reverse('SayaraApi_profile_create')
        data = {
            "is_fabricant": "is_fabricant",
            "is_client": "is_client",
            "Fabricant": create_'sayaraapi_fabricant'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_profile(self):
        profile = create_profile()
        url = reverse('SayaraApi_profile_detail', args=[profile.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_profile(self):
        profile = create_profile()
        data = {
            "is_fabricant": "is_fabricant",
            "is_client": "is_client",
            "Fabricant": create_'sayaraapi_fabricant'().pk,
        }
        url = reverse('SayaraApi_profile_update', args=[profile.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CouleurViewTest(unittest.TestCase):
    '''
    Tests for Couleur
    '''
    def setUp(self):
        self.client = Client()

    def test_list_couleur(self):
        url = reverse('SayaraApi_couleur_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_couleur(self):
        url = reverse('SayaraApi_couleur_create')
        data = {
            "codeCouleur": "codeCouleur",
            "nomCouleur": "nomCouleur",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_couleur(self):
        couleur = create_couleur()
        url = reverse('SayaraApi_couleur_detail', args=[couleur.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_couleur(self):
        couleur = create_couleur()
        data = {
            "codeCouleur": "codeCouleur",
            "nomCouleur": "nomCouleur",
        }
        url = reverse('SayaraApi_couleur_update', args=[couleur.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class OptionViewTest(unittest.TestCase):
    '''
    Tests for Option
    '''
    def setUp(self):
        self.client = Client()

    def test_list_option(self):
        url = reverse('SayaraApi_option_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_option(self):
        url = reverse('SayaraApi_option_create')
        data = {
            "nomOption": "nomOption",
            "codeOption": "codeOption",
            "kilometrage": "kilometrage",
            "date": "date",
            "disponible": "disponible",
            "idFabricant": create_'sayaraapi_fabricant'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_option(self):
        option = create_option()
        url = reverse('SayaraApi_option_detail', args=[option.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_option(self):
        option = create_option()
        data = {
            "nomOption": "nomOption",
            "codeOption": "codeOption",
            "kilometrage": "kilometrage",
            "date": "date",
            "disponible": "disponible",
            "idFabricant": create_'sayaraapi_fabricant'().pk,
        }
        url = reverse('SayaraApi_option_update', args=[option.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RefVersionViewTest(unittest.TestCase):
    '''
    Tests for RefVersion
    '''
    def setUp(self):
        self.client = Client()

    def test_list_refversion(self):
        url = reverse('SayaraApi_refversion_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_refversion(self):
        url = reverse('SayaraApi_refversion_create')
        data = {
            "nom": "nom",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_refversion(self):
        refversion = create_refversion()
        url = reverse('SayaraApi_refversion_detail', args=[refversion.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_refversion(self):
        refversion = create_refversion()
        data = {
            "nom": "nom",
        }
        url = reverse('SayaraApi_refversion_update', args=[refversion.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ImageViewTest(unittest.TestCase):
    '''
    Tests for Image
    '''
    def setUp(self):
        self.client = Client()

    def test_list_image(self):
        url = reverse('SayaraApi_image_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_image(self):
        url = reverse('SayaraApi_image_create')
        data = {
            "image": "image",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_image(self):
        image = create_image()
        url = reverse('SayaraApi_image_detail', args=[image.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_image(self):
        image = create_image()
        data = {
            "image": "image",
        }
        url = reverse('SayaraApi_image_update', args=[image.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RefModeleViewTest(unittest.TestCase):
    '''
    Tests for RefModele
    '''
    def setUp(self):
        self.client = Client()

    def test_list_refmodele(self):
        url = reverse('SayaraApi_refmodele_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_refmodele(self):
        url = reverse('SayaraApi_refmodele_create')
        data = {
            "nom": "nom",
            "marque": create_marque().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_refmodele(self):
        refmodele = create_refmodele()
        url = reverse('SayaraApi_refmodele_detail', args=[refmodele.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_refmodele(self):
        refmodele = create_refmodele()
        data = {
            "nom": "nom",
            "marque": create_marque().pk,
        }
        url = reverse('SayaraApi_refmodele_update', args=[refmodele.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class fabricantViewTest(unittest.TestCase):
    '''
    Tests for fabricant
    '''
    def setUp(self):
        self.client = Client()

    def test_list_fabricant(self):
        url = reverse('SayaraApi_fabricant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_fabricant(self):
        url = reverse('SayaraApi_fabricant_create')
        data = {
            "nom": "nom",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_fabricant(self):
        fabricant = create_fabricant()
        url = reverse('SayaraApi_fabricant_detail', args=[fabricant.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_fabricant(self):
        fabricant = create_fabricant()
        data = {
            "nom": "nom",
        }
        url = reverse('SayaraApi_fabricant_update', args=[fabricant.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RefCouleurViewTest(unittest.TestCase):
    '''
    Tests for RefCouleur
    '''
    def setUp(self):
        self.client = Client()

    def test_list_refcouleur(self):
        url = reverse('SayaraApi_refcouleur_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_refcouleur(self):
        url = reverse('SayaraApi_refcouleur_create')
        data = {
            "nom": "nom",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_refcouleur(self):
        refcouleur = create_refcouleur()
        url = reverse('SayaraApi_refcouleur_detail', args=[refcouleur.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_refcouleur(self):
        refcouleur = create_refcouleur()
        data = {
            "nom": "nom",
        }
        url = reverse('SayaraApi_refcouleur_update', args=[refcouleur.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RefOptionViewTest(unittest.TestCase):
    '''
    Tests for RefOption
    '''
    def setUp(self):
        self.client = Client()

    def test_list_refoption(self):
        url = reverse('SayaraApi_refoption_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_refoption(self):
        url = reverse('SayaraApi_refoption_create')
        data = {
            "nom": "nom",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_refoption(self):
        refoption = create_refoption()
        url = reverse('SayaraApi_refoption_detail', args=[refoption.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_refoption(self):
        refoption = create_refoption()
        data = {
            "nom": "nom",
        }
        url = reverse('SayaraApi_refoption_update', args=[refoption.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LigneTarifViewTest(unittest.TestCase):
    '''
    Tests for LigneTarif
    '''
    def setUp(self):
        self.client = Client()

    def test_list_lignetarif(self):
        url = reverse('SayaraApi_lignetarif_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_lignetarif(self):
        url = reverse('SayaraApi_lignetarif_create')
        data = {
            "dateDebut": "dateDebut",
            "dateFin": "dateFin",
            "prix": "prix",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_lignetarif(self):
        lignetarif = create_lignetarif()
        url = reverse('SayaraApi_lignetarif_detail', args=[lignetarif.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_lignetarif(self):
        lignetarif = create_lignetarif()
        data = {
            "dateDebut": "dateDebut",
            "dateFin": "dateFin",
            "prix": "prix",
        }
        url = reverse('SayaraApi_lignetarif_update', args=[lignetarif.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class FicheTechniqueViewTest(unittest.TestCase):
    '''
    Tests for FicheTechnique
    '''
    def setUp(self):
        self.client = Client()

    def test_list_fichetechnique(self):
        url = reverse('SayaraApi_fichetechnique_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_fichetechnique(self):
        url = reverse('SayaraApi_fichetechnique_create')
        data = {
            "nombrePortes": "nombrePortes",
            "boiteVitesse": "boiteVitesse",
            "puissanceFiscale": "puissanceFiscale",
            "motorisation": "motorisation",
            "consommation": "consommation",
            "dimensions": "dimensions",
            "transmission": "transmission",
            "capaciteReservoir": "capaciteReservoir",
            "vitesseMaxi": "vitesseMaxi",
            "acceleration": "acceleration",
            "images": create_image().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_fichetechnique(self):
        fichetechnique = create_fichetechnique()
        url = reverse('SayaraApi_fichetechnique_detail', args=[fichetechnique.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_fichetechnique(self):
        fichetechnique = create_fichetechnique()
        data = {
            "nombrePortes": "nombrePortes",
            "boiteVitesse": "boiteVitesse",
            "puissanceFiscale": "puissanceFiscale",
            "motorisation": "motorisation",
            "consommation": "consommation",
            "dimensions": "dimensions",
            "transmission": "transmission",
            "capaciteReservoir": "capaciteReservoir",
            "vitesseMaxi": "vitesseMaxi",
            "acceleration": "acceleration",
            "images": create_image().pk,
        }
        url = reverse('SayaraApi_fichetechnique_update', args=[fichetechnique.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


