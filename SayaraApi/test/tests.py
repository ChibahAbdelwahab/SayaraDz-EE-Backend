import unittest
from django.test import Client
from django.contrib.auth.models import User
from rest_framework.test import APIClient

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
