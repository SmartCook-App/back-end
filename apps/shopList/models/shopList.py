from django.db import models


class ShopList(models.Model):
    class Meta:
        db_table = 'shoplist'

    is_completed = models.BooleanField(blank=True, null=True)
    ingredient = models.ManyToManyField(
        'ingredient.Ingredient', through='IngredientShopList',  through_fields=('shopList_id', 'ingredient_id'), related_name='shop_lists'
    )


class IngredientShopList(models.Model):
    ingredient = models.ForeignKey(
        'ingredient.Ingredient', on_delete=models.CASCADE, related_name='ingredient_shop_lists')
    shopList = models.ForeignKey(
        'shopList.ShopList', on_delete=models.CASCADE, related_name='shop_list_ingredients')
    amount = models.FloatField()
