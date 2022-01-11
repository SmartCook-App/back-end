from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    time = models.PositiveIntegerField()
    tips = models.TextField(max_length=200)
    image = models.CharField(max_length=200)
    calories = models.FloatField()
    fat = models.FloatField()
    proteins = models.FloatField()
    carbs = models.FloatField()
    portions = models.PositiveIntegerField()

    owner = models.ForeignKey('user.User', on_delete=models.CASCADE,
                              related_name='owner')

    def __str__(self):
        return self.name
