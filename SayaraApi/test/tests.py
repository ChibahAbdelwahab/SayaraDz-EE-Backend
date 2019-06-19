import unittest
from rest_framework import status
from django.urls import include, path, reverse
from django.test import Client
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase, URLPatternsTestCase
from SayaraApi.models import *
#Test for unauthentified client request
class unAuthentifiedUserRequest(unittest.TestCase):
    def test_detail(self):
        client = Client()
        response = client.get('/api/marque/')
        self.assertEqual(response.status_code, 403)


#Test for Authentified client request
class authentifiedUserRequest(unittest.TestCase):
    def test_detail(self):
        user = User(username='testName')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get("/api/marque/")
        self.assertEqual(response.status_code,200)

class modeleCRUDtest(APITestCase):
     def test_create_modele(self):
        url = reverse("SayaraApi_marque_create")
        data = {"nomModele" : "Modele1",
                "codeModele" : "code",
                "marqueModele" : "marque1",
                "couleurCompatible" : []}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Modele.objects.count(), 1)
        self.assertEqual(Modele.objects.get().name, 'Modele1')
