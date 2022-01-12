from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    time = models.PositiveIntegerField()
    tips = models.TextField(max_length=200)
    image = models.CharField(max_length=200)
    calories = models.FloatField()
    fat = models.FloatField()
    proteins = models.FloatField()
    carbs = models.FloatField()
    portions = models.PositiveIntegerField()

    owner = models.ForeignKey('user.User', on_delete=models.CASCADE,
                              related_name='owner')

    notes = models.ManyToManyField(
        'user.User', through='recipeNotes', through_fields=('recipe_id', 'user_id'))

    notes = models.ManyToManyField(
        'user.User', through='LastTimeCooked', through_fields=('recipe_id', 'user_id'))

    def __str__(self):
        return self.name


class RecipeNotes(models.Model):
    recipe_id = models.ForeignKey(
        'recipe.Recipe', on_delete=models.CASCADE, related_name='recipe_id_recipeNotes')
    user_id = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='user_id_recipeNotes')
    note = models.TextField(max_length=200)


class LastTimeCooked(models.Model):
    recipe_id = models.ForeignKey(
        'recipe.Recipe', on_delete=models.CASCADE, related_name='recipe_id_lastTimeCooked')
    user_id = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='user_id_lastTimeCooked')
    lastTimeCooked = models.PositiveIntegerField()
