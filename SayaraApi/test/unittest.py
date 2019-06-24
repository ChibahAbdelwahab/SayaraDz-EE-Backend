import unittest
from django.urls import reverse
from django.test import Client
from .models import Image, Vehicule, Marque, RefVersion, Version, RefModele, Modele, Annonce, Fabricant, Profile, RefCouleur, Couleur, RefOption, Option, LigneTarif, FicheTechnique
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


def create_image(**kwargs):
    defaults = {}
    defaults["image"] = "image"
    defaults.update(**kwargs)
    return Image.objects.create(**defaults)


def create_vehicule(**kwargs):
    defaults = {}
    defaults["num"] = "num"
    defaults["vehicule"] = "vehicule"
    defaults.update(**kwargs)
    return Vehicule.objects.create(**defaults)


def create_marque(**kwargs):
    defaults = {}
    defaults["nom"] = "nom"
    defaults["image"] = "image"
    defaults.update(**kwargs)
    return Marque.objects.create(**defaults)


def create_refversion(**kwargs):
    defaults = {}
    defaults["nom"] = "nom"
    defaults.update(**kwargs)
    return RefVersion.objects.create(**defaults)


def create_version(**kwargs):
    defaults = {}
    defaults["code"] = "code"
    defaults["prix_base"] = "prix_base"
    defaults.update(**kwargs)
    if "nom" not in defaults:
        defaults["nom"] = create_refversion()
    if "images" not in defaults:
        defaults["images"] = create_image()
    if "options" not in defaults:
        defaults["options"] = create_'sayaraapi_option'()
    if "modele" not in defaults:
        defaults["modele"] = create_'sayaraapi_modele'()
    if "ficheTechnique" not in defaults:
        defaults["ficheTechnique"] = create_"sayaraapi_fichetechnique"()
    if "couleur" not in defaults:
        defaults["couleur"] = create_"sayaraapi_couleur"()
    return Version.objects.create(**defaults)


def create_refmodele(**kwargs):
    defaults = {}
    defaults["nom"] = "nom"
    defaults.update(**kwargs)
    if "marque" not in defaults:
        defaults["marque"] = create_marque()
    return RefModele.objects.create(**defaults)


def create_modele(**kwargs):
    defaults = {}
    defaults["code"] = "code"
    defaults["image"] = "image"
    defaults.update(**kwargs)
    if "nom" not in defaults:
        defaults["nom"] = create_refmodele()
    return Modele.objects.create(**defaults)


def create_annonce(**kwargs):
    defaults = {}
    defaults["titre"] = "titre"
    defaults["prix"] = "prix"
    defaults["commentaires"] = "commentaires"
    defaults.update(**kwargs)
    if "vehicule" not in defaults:
        defaults["vehicule"] = create_'sayaraapi_vehiculeoccasion'()
    if "user" not in defaults:
        defaults["user"] = create_user()
    return Annonce.objects.create(**defaults)


def create_fabricant(**kwargs):
    defaults = {}
    defaults["nom"] = "nom"
    defaults.update(**kwargs)
    return Fabricant.objects.create(**defaults)


def create_profile(**kwargs):
    defaults = {}
    defaults["is_fabricant"] = "is_fabricant"
    defaults["is_client"] = "is_client"
    defaults.update(**kwargs)
    if "fabricant" not in defaults:
        defaults["fabricant"] = create_'sayaraapi_fabricant'()
    return Profile.objects.create(**defaults)


def create_refcouleur(**kwargs):
    defaults = {}
    defaults["nom"] = "nom"
    defaults.update(**kwargs)
    return RefCouleur.objects.create(**defaults)


def create_couleur(**kwargs):
    defaults = {}
    defaults["code"] = "code"
    defaults.update(**kwargs)
    if "nom" not in defaults:
        defaults["nom"] = create_refcouleur()
    if "modele" not in defaults:
        defaults["modele"] = create_'sayaraapi_modele'()
    return Couleur.objects.create(**defaults)


def create_refoption(**kwargs):
    defaults = {}
    defaults["nom"] = "nom"
    defaults.update(**kwargs)
    return RefOption.objects.create(**defaults)


def create_option(**kwargs):
    defaults = {}
    defaults["code"] = "code"
    defaults["kilometrage"] = "kilometrage"
    defaults["date"] = "date"
    defaults["image1"] = "image1"
    defaults["image2"] = "image2"
    defaults["image3"] = "image3"
    defaults["disponible"] = "disponible"
    defaults["reserve"] = "reserve"
    defaults["concessionnaire"] = "concessionnaire"
    defaults.update(**kwargs)
    if "nom" not in defaults:
        defaults["nom"] = create_refoption()
    if "modele" not in defaults:
        defaults["modele"] = create_'sayaraapi_modele'()
    if "version" not in defaults:
        defaults["version"] = create_refversion()
    if "model" not in defaults:
        defaults["model"] = create_refmodele()
    if "options" not in defaults:
        defaults["options"] = create_refoption()
    if "version" not in defaults:
        defaults["version"] = create_version()
    if "options" not in defaults:
        defaults["options"] = create_option()
    if "couleur" not in defaults:
        defaults["couleur"] = create_couleur()
    return Option.objects.create(**defaults)


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
    return FicheTechnique.objects.create(**defaults)


class ImageViewTest(unittest.TestCase):
    '''
    Tests for Image
    '''
    def setUp(self):
        self.client = Client()

    def test_list_image(self):
        url = reverse('app_name_image_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_image(self):
        url = reverse('app_name_image_create')
        data = {
            "image": "image",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_image(self):
        image = create_image()
        url = reverse('app_name_image_detail', args=[image.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_image(self):
        image = create_image()
        data = {
            "image": "image",
        }
        url = reverse('app_name_image_update', args=[image.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class VehiculeViewTest(unittest.TestCase):
    '''
    Tests for Vehicule
    '''
    def setUp(self):
        self.client = Client()

    def test_list_vehicule(self):
        url = reverse('app_name_vehicule_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_vehicule(self):
        url = reverse('app_name_vehicule_create')
        data = {
            "num": "num",
            "vehicule": "vehicule",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_vehicule(self):
        vehicule = create_vehicule()
        url = reverse('app_name_vehicule_detail', args=[vehicule.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_vehicule(self):
        vehicule = create_vehicule()
        data = {
            "num": "num",
            "vehicule": "vehicule",
        }
        url = reverse('app_name_vehicule_update', args=[vehicule.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class MarqueViewTest(unittest.TestCase):
    '''
    Tests for Marque
    '''
    def setUp(self):
        self.client = Client()

    def test_list_marque(self):
        url = reverse('app_name_marque_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_marque(self):
        url = reverse('app_name_marque_create')
        data = {
            "nom": "nom",
            "image": "image",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_marque(self):
        marque = create_marque()
        url = reverse('app_name_marque_detail', args=[marque.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_marque(self):
        marque = create_marque()
        data = {
            "nom": "nom",
            "image": "image",
        }
        url = reverse('app_name_marque_update', args=[marque.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RefVersionViewTest(unittest.TestCase):
    '''
    Tests for RefVersion
    '''
    def setUp(self):
        self.client = Client()

    def test_list_refversion(self):
        url = reverse('app_name_refversion_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_refversion(self):
        url = reverse('app_name_refversion_create')
        data = {
            "nom": "nom",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_refversion(self):
        refversion = create_refversion()
        url = reverse('app_name_refversion_detail', args=[refversion.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_refversion(self):
        refversion = create_refversion()
        data = {
            "nom": "nom",
        }
        url = reverse('app_name_refversion_update', args=[refversion.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class VersionViewTest(unittest.TestCase):
    '''
    Tests for Version
    '''
    def setUp(self):
        self.client = Client()

    def test_list_version(self):
        url = reverse('app_name_version_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_version(self):
        url = reverse('app_name_version_create')
        data = {
            "code": "code",
            "prix_base": "prix_base",
            "nom": create_refversion().pk,
            "images": create_image().pk,
            "options": create_'sayaraapi_option'().pk,
            "modele": create_'sayaraapi_modele'().pk,
            "ficheTechnique": create_"sayaraapi_fichetechnique"().pk,
            "couleur": create_"sayaraapi_couleur"().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_version(self):
        version = create_version()
        url = reverse('app_name_version_detail', args=[version.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_version(self):
        version = create_version()
        data = {
            "code": "code",
            "prix_base": "prix_base",
            "nom": create_refversion().pk,
            "images": create_image().pk,
            "options": create_'sayaraapi_option'().pk,
            "modele": create_'sayaraapi_modele'().pk,
            "ficheTechnique": create_"sayaraapi_fichetechnique"().pk,
            "couleur": create_"sayaraapi_couleur"().pk,
        }
        url = reverse('app_name_version_update', args=[version.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RefModeleViewTest(unittest.TestCase):
    '''
    Tests for RefModele
    '''
    def setUp(self):
        self.client = Client()

    def test_list_refmodele(self):
        url = reverse('app_name_refmodele_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_refmodele(self):
        url = reverse('app_name_refmodele_create')
        data = {
            "nom": "nom",
            "marque": create_marque().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_refmodele(self):
        refmodele = create_refmodele()
        url = reverse('app_name_refmodele_detail', args=[refmodele.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_refmodele(self):
        refmodele = create_refmodele()
        data = {
            "nom": "nom",
            "marque": create_marque().pk,
        }
        url = reverse('app_name_refmodele_update', args=[refmodele.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ModeleViewTest(unittest.TestCase):
    '''
    Tests for Modele
    '''
    def setUp(self):
        self.client = Client()

    def test_list_modele(self):
        url = reverse('app_name_modele_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_modele(self):
        url = reverse('app_name_modele_create')
        data = {
            "code": "code",
            "image": "image",
            "nom": create_refmodele().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_modele(self):
        modele = create_modele()
        url = reverse('app_name_modele_detail', args=[modele.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_modele(self):
        modele = create_modele()
        data = {
            "code": "code",
            "image": "image",
            "nom": create_refmodele().pk,
        }
        url = reverse('app_name_modele_update', args=[modele.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AnnonceViewTest(unittest.TestCase):
    '''
    Tests for Annonce
    '''
    def setUp(self):
        self.client = Client()

    def test_list_annonce(self):
        url = reverse('app_name_annonce_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_annonce(self):
        url = reverse('app_name_annonce_create')
        data = {
            "titre": "titre",
            "prix": "prix",
            "commentaires": "commentaires",
            "vehicule": create_'sayaraapi_vehiculeoccasion'().pk,
            "user": create_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_annonce(self):
        annonce = create_annonce()
        url = reverse('app_name_annonce_detail', args=[annonce.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_annonce(self):
        annonce = create_annonce()
        data = {
            "titre": "titre",
            "prix": "prix",
            "commentaires": "commentaires",
            "vehicule": create_'sayaraapi_vehiculeoccasion'().pk,
            "user": create_user().pk,
        }
        url = reverse('app_name_annonce_update', args=[annonce.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class FabricantViewTest(unittest.TestCase):
    '''
    Tests for Fabricant
    '''
    def setUp(self):
        self.client = Client()

    def test_list_fabricant(self):
        url = reverse('app_name_fabricant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_fabricant(self):
        url = reverse('app_name_fabricant_create')
        data = {
            "nom": "nom",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_fabricant(self):
        fabricant = create_fabricant()
        url = reverse('app_name_fabricant_detail', args=[fabricant.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_fabricant(self):
        fabricant = create_fabricant()
        data = {
            "nom": "nom",
        }
        url = reverse('app_name_fabricant_update', args=[fabricant.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProfileViewTest(unittest.TestCase):
    '''
    Tests for Profile
    '''
    def setUp(self):
        self.client = Client()

    def test_list_profile(self):
        url = reverse('app_name_profile_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_profile(self):
        url = reverse('app_name_profile_create')
        data = {
            "is_fabricant": "is_fabricant",
            "is_client": "is_client",
            "fabricant": create_'sayaraapi_fabricant'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_profile(self):
        profile = create_profile()
        url = reverse('app_name_profile_detail', args=[profile.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_profile(self):
        profile = create_profile()
        data = {
            "is_fabricant": "is_fabricant",
            "is_client": "is_client",
            "fabricant": create_'sayaraapi_fabricant'().pk,
        }
        url = reverse('app_name_profile_update', args=[profile.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RefCouleurViewTest(unittest.TestCase):
    '''
    Tests for RefCouleur
    '''
    def setUp(self):
        self.client = Client()

    def test_list_refcouleur(self):
        url = reverse('app_name_refcouleur_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_refcouleur(self):
        url = reverse('app_name_refcouleur_create')
        data = {
            "nom": "nom",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_refcouleur(self):
        refcouleur = create_refcouleur()
        url = reverse('app_name_refcouleur_detail', args=[refcouleur.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_refcouleur(self):
        refcouleur = create_refcouleur()
        data = {
            "nom": "nom",
        }
        url = reverse('app_name_refcouleur_update', args=[refcouleur.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CouleurViewTest(unittest.TestCase):
    '''
    Tests for Couleur
    '''
    def setUp(self):
        self.client = Client()

    def test_list_couleur(self):
        url = reverse('app_name_couleur_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_couleur(self):
        url = reverse('app_name_couleur_create')
        data = {
            "code": "code",
            "nom": create_refcouleur().pk,
            "modele": create_'sayaraapi_modele'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_couleur(self):
        couleur = create_couleur()
        url = reverse('app_name_couleur_detail', args=[couleur.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_couleur(self):
        couleur = create_couleur()
        data = {
            "code": "code",
            "nom": create_refcouleur().pk,
            "modele": create_'sayaraapi_modele'().pk,
        }
        url = reverse('app_name_couleur_update', args=[couleur.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RefOptionViewTest(unittest.TestCase):
    '''
    Tests for RefOption
    '''
    def setUp(self):
        self.client = Client()

    def test_list_refoption(self):
        url = reverse('app_name_refoption_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_refoption(self):
        url = reverse('app_name_refoption_create')
        data = {
            "nom": "nom",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_refoption(self):
        refoption = create_refoption()
        url = reverse('app_name_refoption_detail', args=[refoption.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_refoption(self):
        refoption = create_refoption()
        data = {
            "nom": "nom",
        }
        url = reverse('app_name_refoption_update', args=[refoption.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class OptionViewTest(unittest.TestCase):
    '''
    Tests for Option
    '''
    def setUp(self):
        self.client = Client()

    def test_list_option(self):
        url = reverse('app_name_option_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_option(self):
        url = reverse('app_name_option_create')
        data = {
            "code": "code",
            "kilometrage": "kilometrage",
            "date": "date",
            "image1": "image1",
            "image2": "image2",
            "image3": "image3",
            "disponible": "disponible",
            "reserve": "reserve",
            "concessionnaire": "concessionnaire",
            "nom": create_refoption().pk,
            "modele": create_'sayaraapi_modele'().pk,
            "version": create_refversion().pk,
            "model": create_refmodele().pk,
            "options": create_refoption().pk,
            "version": create_version().pk,
            "options": create_option().pk,
            "couleur": create_couleur().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_option(self):
        option = create_option()
        url = reverse('app_name_option_detail', args=[option.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_option(self):
        option = create_option()
        data = {
            "code": "code",
            "kilometrage": "kilometrage",
            "date": "date",
            "image1": "image1",
            "image2": "image2",
            "image3": "image3",
            "disponible": "disponible",
            "reserve": "reserve",
            "concessionnaire": "concessionnaire",
            "nom": create_refoption().pk,
            "modele": create_'sayaraapi_modele'().pk,
            "version": create_refversion().pk,
            "model": create_refmodele().pk,
            "options": create_refoption().pk,
            "version": create_version().pk,
            "options": create_option().pk,
            "couleur": create_couleur().pk,
        }
        url = reverse('app_name_option_update', args=[option.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LigneTarifViewTest(unittest.TestCase):
    '''
    Tests for LigneTarif
    '''
    def setUp(self):
        self.client = Client()

    def test_list_lignetarif(self):
        url = reverse('app_name_lignetarif_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_lignetarif(self):
        url = reverse('app_name_lignetarif_create')
        data = {
            "dateDebut": "dateDebut",
            "dateFin": "dateFin",
            "prix": "prix",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_lignetarif(self):
        lignetarif = create_lignetarif()
        url = reverse('app_name_lignetarif_detail', args=[lignetarif.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_lignetarif(self):
        lignetarif = create_lignetarif()
        data = {
            "dateDebut": "dateDebut",
            "dateFin": "dateFin",
            "prix": "prix",
        }
        url = reverse('app_name_lignetarif_update', args=[lignetarif.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class FicheTechniqueViewTest(unittest.TestCase):
    '''
    Tests for FicheTechnique
    '''
    def setUp(self):
        self.client = Client()

    def test_list_fichetechnique(self):
        url = reverse('app_name_fichetechnique_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_fichetechnique(self):
        url = reverse('app_name_fichetechnique_create')
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
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_fichetechnique(self):
        fichetechnique = create_fichetechnique()
        url = reverse('app_name_fichetechnique_detail', args=[fichetechnique.pk,])
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
        }
        url = reverse('app_name_fichetechnique_update', args=[fichetechnique.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


