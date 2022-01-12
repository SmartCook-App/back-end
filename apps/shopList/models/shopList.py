from django.db import models


class ShopList(models.Model):
    is_completed = models.BooleanField(blank=True, null=True)
    # ingredient_id = models.ManyToManyField(
    #     'ingredientShopList.IngredientShopList')

    def __str__(self):
        return self.id
