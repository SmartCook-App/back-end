from rest_framework import serializers
from ..models.dishCategory import DishCategory


class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishCategory
        fields = ['id', 'name', 'image', 'dish_category_intermediate']