from django.db import models

# Create your models here.


class Produit(models.Model):
    produitRef = models.CharField(max_length=30)
    nomProduit = models.CharField(max_length=30)
    dateProduction = models.DateField()
    prix = models.FloatField()


class Commande(models.Model):
    referenceCmd = models.CharField(max_length=30)
    dateCmd = models.DateField()


class Personne(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.CharField(max_length=30)


class Categorie(models.Model):
    nomCategorie = models.CharField(max_length=30)
