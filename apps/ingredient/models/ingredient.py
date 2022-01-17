from django.db import models
from django.db.models.deletion import CASCADE


class Ingredient(models.Model):
    ingredient_category_id = models.ForeignKey(
        'ingredientCategory.IngredientCategory', on_delete=models.CASCADE, related_name='ingredient_category_id')
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# class IngredientShopList(models.Model):
#     shop_list_id = models.ForeignKey(
#         'shopList.ShopList', on_delete=models.CASCADE, related_name='shop_lists_ingredients')
#     ingredient_id = models.ForeignKey(
#         'ingredient.Ingredient', on_delete=models.CASCADE, related_name='ingredients_from_shop_lists')
#     amount = models.FloatField()
