from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase
from SayaraApi.models import *
from rest_framework.test import APITestCase, force_authenticate


class AnnoncesTestCases(APITestCase):
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
            "version": "Tech Vision",
            "modele": 34,
            "options": [
                1
            ]
        }
        response = self.client.post('/api/vehiculeoccasion/create/', data,
                                    format='json')

        self.assertEqual(response.status_code, 201)

    def test_AnnonceOcasion_create(self):
        data = {
            "titre": "Test inseriton de l'annonce",
            "prix": 4567,
            "commentaires": "Ceci est un text aleatoire juste pour tester",
            "vehicule": 3,
        }
        response = self.client.post('/api/annonce/create/', data, format='json')

        self.assertEqual(response.status_code, 201)
