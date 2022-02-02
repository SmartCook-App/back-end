from ..serializers import RecipeSerializer
from ..models.recipe import Recipe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Para todas las recetas


class Recipe_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        recipe = Recipe.objects.all()
        serializer = RecipeSerializer(recipe, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Para una receta en específico

class Recipe_APIView_Detail(APIView):
    def get_id(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        recipe = self.get_id(pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        recipe = self.get_id(pk)
        serializer = RecipeSerializer(recipe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipe = self.get_id(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
