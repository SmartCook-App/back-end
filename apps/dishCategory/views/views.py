from ..serializers import DishCategorySerializer
from ..models.dishCategory import DishCategory
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from apps.dishCategory import serializers


class DishCategory_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        dish_categories = DishCategory.objects.all()
        serializer = DishCategorySerializer(dish_categories, many=True)
        return Response(serializer.data)

class DishCategory_APIView_Detail(APIView):
    def get_id(self, pk):
        try:
            return DishCategory.objects.get(pk=pk)
        except DishCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dish_category = self.get_id(pk)
        serializer = DishCategorySerializer(dish_category)
        return Response(serializer.data)