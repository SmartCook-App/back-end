from django.db import models


class ShopList(models.Model):
    is_completed = models.BooleanField(blank=True, null=True)
    # ingredient_id_shopList = models.ForeignKey('ingredient.Ingredient', on_delete=models.CASCADE,
    #                                            related_name='ingredient_id_shopList')

    # def __str__(self):
    #     return self.name
