from __future__ import unicode_literals  
from django.db import models  

# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=20)
    categorie = models.CharField(max_length=20)
    prix = models.IntegerField()
    
    class Meta:
        db_table = "Produit"
