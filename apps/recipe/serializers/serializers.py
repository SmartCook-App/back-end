from rest_framework import serializers
from ..models.recipe import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'time', 'tips', 'image', 'calories', 'fat',
                  'proteins', 'carbs', 'difficulty', 'portions', 'owner']
