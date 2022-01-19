from django.db import models


class Step(models.Model):
    step_number = models.IntegerField(default=None)
    description = models.TextField(max_length=200)
    image = models.CharField(max_length=200)

    recipe = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE,
                               related_name='recipe_step', default=None)

    def __str__(self):
        return self.name
