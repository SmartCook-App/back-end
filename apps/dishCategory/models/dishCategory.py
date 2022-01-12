from django.db import models


class DishCategory(models.Model):
    name = models.CharField(max_length=200)
    recipe_id_dishCategory = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE,
                                               related_name='recipe_id_dishCategory')

    def __str__(self):
        return self.name
