from django import forms
from .models import Vehicule, Marque, Version, Modele


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = []


class MarqueForm(forms.ModelForm):
    class Meta:
        model = Marque
        fields = ['idMarque', 'nomMarque']


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['nomVersion', 'codeVersion', 'modeleVersion']


class ModeleForm(forms.ModelForm):
    class Meta:
        model = Modele
        fields = ['nomModele', 'idModele', 'marqueModele']


