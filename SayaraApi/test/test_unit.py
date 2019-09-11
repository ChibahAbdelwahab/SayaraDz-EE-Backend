
from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase
from SayaraApi.models import *
from rest_framework.test import APITestCase, force_authenticate


class test_create(APITestCase):
    def setUp(self):
        call_command('loaddata', 'db3.json', verbosity=0)
        self.username = 'uservw1'
        self.password = 'password123.'
        self.client.force_authenticate(self.username)
        print(self.client)

    def test_VehiculeOccasion_create(self):
        data = {
            "id": 3,
            "kilometrage": 3456,
            "date": "2019-09-18",
            "couleur": "Bleu",
            "version": "g7memphis",
            "modele": 34,
            "options": [
                1
            ]
        }
        response = self.client.post('/api/vehiculeoccasion/create/', data,
                                    format='json')

        self.assertEqual(response.status_code, 201)

    def test_refversion_create(self):
        data = {
            "nom": "testversion",
        }
        response = self.client.post('/api/refversion/create/', data, format='json')

        self.assertEqual(response.status_code, 201)

    def test_refmodele_create(self):
        data = {
            "nom": "testmodele",
            "marque":"1"
        }
        response = self.client.post('/api/refmodele/create/', data, format='json')

        self.assertEqual(response.status_code, 201)

    def test_refcouleur_create(self):
        data = {
            "nom": "testcouleur",
        }
        response = self.client.post('/api/refcouleur/create/', data, format='json')

        self.assertEqual(response.status_code, 201)


    # def test_couleur_create(self):
    #     data = {
    #             "code": "b02",
    #             "modele": 2,
    #             "prix": 50000
    #     }
    #     response = self.client.post('/api/refcouleur/create/', data, format='json')
    #     self.assertEqual(response.status_code, 201)


class test_list(APITestCase):
    def setUp(self):
        call_command('loaddata', 'db3.json', verbosity=0)
        self.username = 'uservw1'
        self.password = 'password123.'
        self.client.force_authenticate(self.username)
        print(self.client)

    def test_annonceneuf_list(self):
        response = self.client.get('/api/annonce/neuf/')
        self.assertEqual(response.status_code, 200)

    def test_annonceoccasion_list(self):
        response = self.client.get('/api/annonce/occasion/')
        self.assertEqual(response.status_code, 200)

    def test_marque_list(self):
        response = self.client.get('/api/marque/')
        self.assertEqual(response.status_code, 200)

    def test_modele_list(self):
        response = self.client.get('/api/modele/')
        self.assertEqual(response.status_code, 200)

    def test_refmodele_list(self):
        response = self.client.get('/api/refmodele/')
        self.assertEqual(response.status_code, 200)

    def test_version_list(self):
        response = self.client.get('/api/version/')
        self.assertEqual(response.status_code, 200)

    def test_refversion_list(self):
        response = self.client.get('/api/refversion/')
        self.assertEqual(response.status_code, 200)

    def test_couleur_list(self):
        response = self.client.get('/api/couleur/')
        self.assertEqual(response.status_code, 200)

    def test_refcouleur_list(self):
        response = self.client.get('/api/refcouleur/')
        self.assertEqual(response.status_code, 200)

    def test_option_list(self):
        response = self.client.get('/api/option/')
        self.assertEqual(response.status_code, 200)

    def test_fichetechnique_list(self):
        response = self.client.get('/api/fichetechnique/')
        self.assertEqual(response.status_code, 200)




    # def test_refoption_list(self):
    #     response = self.client.get('/api/refoption/')
    #     self.assertEqual(response.status_code, 200)



