from dataclasses import fields
from django import forms
from produits.models import Produit

class ProdForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"