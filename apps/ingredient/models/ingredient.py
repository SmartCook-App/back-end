from django.db import models
from django.db.models.deletion import CASCADE


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class IngredientShopList(Ingredient):
    shopList_id = models.ForeignKey(
        'shopList.ShopList', on_delete=CASCADE, related_name='shoplist_id_ingredientShopList')
    amount = models.FloatField()


class IngredientRecipe(Ingredient):
    recipe_id = models.ForeignKey(
        'recipe.Recipe', on_delete=CASCADE, related_name='recipe_id_ingredientRecipe')
    amount = models.FloatField()
