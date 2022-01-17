from django.db import models


class Step(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    image = models.CharField(max_length=200)

    recipe_id = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE,
                                  related_name='recipe_id')

    def __str__(self):
        return self.name
