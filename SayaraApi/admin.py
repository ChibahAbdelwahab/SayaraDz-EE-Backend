from django.contrib import admin
from django import forms
from .models import Vehicule, Marque, Version, Modele

admin.site.register(Vehicule)
admin.site.register(Marque)
admin.site.register(Version)
admin.site.register(Modele)