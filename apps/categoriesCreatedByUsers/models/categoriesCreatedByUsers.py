from django.db import models


class CategoriesCreatedByUsers(models.Model):

    category_name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name
