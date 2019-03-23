from rest_framework import authentication
from django.contrib.auth.models import User
from rest_framework import exceptions

import os
from django.conf import settings

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

json = os.path.join(settings.BASE_DIR, settings.FIREBASE_KEY)

cred = credentials.Certificate(json)
firebase_admin.initialize_app(cred)


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        id_token = request.META.get('HTTP_AUTHORIZATION')
        # print(request.META.get('HTTP_AUTHORIZATION'))
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
            # print(decoded_token)
        except Exception as e:
            print('Exception: ', e)
            pass

        if not id_token or not decoded_token:
            return None

        uid = decoded_token.get('uid')
        name = decoded_token.get('name')
        email = decoded_token.get('email')
        user, bool = User.objects.get_or_create(username=name, email=email)
        return (user, None)
