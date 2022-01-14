from django.db import models
from django.db.models.deletion import CASCADE


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name
