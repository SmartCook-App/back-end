from django.db import models


class Recipe(models.Model):
    class Meta:
        db_table = 'recipe'

    name = models.CharField(max_length=200)
    time = models.PositiveIntegerField()
    tips = models.TextField(max_length=200)
    image = models.CharField(max_length=200)
    calories = models.FloatField()
    fat = models.FloatField()
    proteins = models.FloatField()
    carbs = models.FloatField()
    difficulty = models.CharField(max_length=200, default='None')
    portions = models.PositiveIntegerField()

    owner = models.ForeignKey('user.User', on_delete=models.CASCADE,
                              related_name='owner')

    notes = models.ManyToManyField(
        'user.User', through='recipeNotes', through_fields=('recipe_id', 'user_id'), related_name='recipes_notes')

    lastDateCooked = models.ManyToManyField(
        'user.User', through='LastTimeCooked', through_fields=('recipe_id', 'user_id'), related_name='last_date_cooked_recipes')

    ingredient = models.ManyToManyField(
        'ingredient.Ingredient', through='IngredientRecipe', through_fields=('recipe_id', 'ingredient_id'), related_name='recipe_ingredient')

    def __str__(self):
        return self.name


class RecipeNotes(models.Model):
    class Meta:
        db_table = 'recipe_notes'
    recipe = models.ForeignKey(
        'recipe.Recipe', on_delete=models.CASCADE, related_name='recipe_recipe_notes')
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='user_recipe_notes')
    note = models.TextField(max_length=200)


class LastTimeCooked(models.Model):
    class Meta:
        db_table = 'last_time_cooked'
    recipe = models.ForeignKey(
        'recipe.Recipe', on_delete=models.CASCADE, related_name='recipe_last_date_cooked')
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='user_last_date_cooked')
    lastDateCooked = models.DateField()


class IngredientRecipe(models.Model):
    class Meta:
        db_table = 'ingredient_recipe'
    ingredient = models.ForeignKey(
        'ingredient.Ingredient', on_delete=models.CASCADE, related_name='recipes')
    recipe = models.ForeignKey(
        'recipe.Recipe', on_delete=models.CASCADE, related_name='recipe_ingredients_middle_table')
    amount = models.FloatField()
