from django.contrib import admin
from django import forms
from .models import *

admin.site.register(Vehicule)
admin.site.register(Marque)
admin.site.register(Version)
admin.site.register(Modele)
admin.site.register(Annonce)
admin.site.register(Fabricant)
admin.site.register(userAccount)