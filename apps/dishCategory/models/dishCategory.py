from django.db import models
from apps.user.models.user import User


class DishCategory(models.Model):
    name = models.CharField(max_length=200)
    recipe_id_dishCategory = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE,
                                               related_name='recipe_id_dishCategory')

    # This filters belongs to one user and are display in his profile (this is a Many to one relation)
    # user = models.ForeignKey(to='user.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
