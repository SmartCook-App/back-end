from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=[('ml', 'male'), ('fl', 'female')],
                              max_length=10, blank=True, null=True)
    is_cooker = models.BooleanField(blank=True, null=True)

    saved_recipes = models.ManyToManyField('recipe.Recipe')

    liked_recipes = models.ManyToManyField('recipe.Recipe', related_name='liked_recipes')

    follows_user = models.ManyToManyField('user.User')

    def __str__(self):
        return self.get_full_name()
