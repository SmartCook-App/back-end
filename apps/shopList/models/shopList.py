from django.db import models


class ShopList(models.Model):
    is_completed = models.BooleanField(blank=True, null=True)
    ingredient_id = models.ManyToManyField(
        through='ingredient.IngredientShopList', related_name='shop_lists'
    )

    def __str__(self):
        return self.id
