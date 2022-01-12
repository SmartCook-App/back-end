from django.db import models


class Video(models.Model):
    path = models.TextField(max_length=200)

    recipe_id_video = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE,
                                        related_name='recipe_id_video')

    def __str__(self):
        return self.path
