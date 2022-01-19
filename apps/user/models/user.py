from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    class Meta:
        db_table = 'user'
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=[('ml', 'male'), ('fl', 'female')],
                              max_length=10, blank=True, null=True)
    is_cooker = models.BooleanField(blank=True, null=True)

    saved_recipes = models.ManyToManyField('recipe.Recipe')

    liked_recipes = models.ManyToManyField(
        'recipe.Recipe', related_name='liked_recipes')

    follows_user = models.ManyToManyField('user.User')

    user_profile_categories = models.ManyToManyField(
        'recipe.Recipe', through='CategoriesInUserProfile', through_fields=('user_id', 'recipe_id'), related_name='user_profile_categories')

    def __str__(self):
        return self.get_full_name()


class CategoriesInUserProfile(models.Model):
    class Meta:
        db_table = 'categories_in_user_profile'
    recipe = models.ForeignKey(
        'recipe.Recipe', on_delete=models.CASCADE, related_name='recipe_that_belongs_to_user_category')
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='user_that_owns_category')
    category_name = models.ForeignKey(
        'categoriesCreatedByUsers.CategoriesCreatedByUsers', on_delete=models.CASCADE, related_name='category_names')
