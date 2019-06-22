from django import forms
from .models import Vehicule, Marque, Version, Modele


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = []

#some comment
class MarqueForm(forms.ModelForm):
    class Meta:
        model = Marque
        fields = ['nom']


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['nom']


class ModeleForm(forms.ModelForm):
    class Meta:
        model = Modele
        fields = ['nom']


