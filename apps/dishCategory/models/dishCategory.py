from django.db import models
from apps.user.models.user import User


class DishCategory(models.Model):
    class Meta:
        db_table = 'dish_category'
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    dish_category_intermediate = models.ManyToManyField(
        'recipe.Recipe', related_name='dish_categories')

    def __str__(self):
        return self.name
