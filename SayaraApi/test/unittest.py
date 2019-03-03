import unittest
from django.urls import reverse
from django.test import Client
from .models import Vehicule, Marque, Version, Modele
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
    defaults["numChassis"] = "numChassis"
    defaults["disponible"] = "disponible"
    defaults["imageVehicle"] = "imageVehicle"
    defaults.update(**kwargs)
    return Vehicule.objects.create(**defaults)


def create_marque(**kwargs):
    defaults = {}
    defaults["idMarque"] = "idMarque"
    defaults["nomMarque"] = "nomMarque"
    defaults["imageMarque"] = "imageMarque"
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
    defaults["nomModele"] = "nomModele"
    defaults["idModele"] = "idModele"
    defaults.update(**kwargs)
    return Modele.objects.create(**defaults)


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
            "numChassis": "numChassis",
            "disponible": "disponible",
            "imageVehicle": "imageVehicle",
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
            "numChassis": "numChassis",
            "disponible": "disponible",
            "imageVehicle": "imageVehicle",
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
            "idMarque": "idMarque",
            "nomMarque": "nomMarque",
            "imageMarque": "imageMarque",
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
            "idMarque": "idMarque",
            "nomMarque": "nomMarque",
            "imageMarque": "imageMarque",
        }
        url = reverse('app_name_marque_update', args=[marque.pk,])
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
            "nomVersion": "nomVersion",
            "codeVersion": "codeVersion",
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
            "nomVersion": "nomVersion",
            "codeVersion": "codeVersion",
        }
        url = reverse('app_name_version_update', args=[version.pk,])
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
            "nomModele": "nomModele",
            "idModele": "idModele",
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
            "nomModele": "nomModele",
            "idModele": "idModele",
        }
        url = reverse('app_name_modele_update', args=[modele.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)