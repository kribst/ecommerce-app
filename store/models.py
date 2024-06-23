from datetime import datetime

from django.db import models


# Create your models here.

class Vetement(models.Model):
    TYPES = (
        ('homme', 'Homme'),
        ('femme', 'Femme'),
        ('enfant', 'Enfant'),
        ('bebe', 'Bébé'),
    )
    article = models.CharField(max_length=50)
    quantite = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    nouveau_prix = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=TYPES)
    description = models.TextField()
    information_Technique = models.TextField()
    image = models.ImageField()
    publié = models.DateTimeField(default=datetime.now)


