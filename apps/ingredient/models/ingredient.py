from django.db import models
from django.db.models.deletion import CASCADE


class Ingredient(models.Model):
    class Meta:
        db_table = 'ingredient'
    ingredient_category = models.ForeignKey(
        'ingredientCategory.IngredientCategory', on_delete=models.CASCADE, related_name='ingredient_category_id')
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name
