from django.db import models


class ShopList(models.Model):
    is_completed = models.BooleanField(blank=True, null=True)
    # ingredient = models.ForeignKey('shopList.ShopList.', on_delete=models.CASCADE,
    # related_name='ingredient')

    # def __str__(self):
    #     return self.name
