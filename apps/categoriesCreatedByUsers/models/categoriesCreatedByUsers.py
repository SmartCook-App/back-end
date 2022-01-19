from django.db import models


class CategoriesCreatedByUsers(models.Model):

    class Meta:
        db_table = 'categories_created_by_users'

    category_name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name
