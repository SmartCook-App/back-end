from django.db import models


class DailyMenus(models.Model):
    day = models.DateField()
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='user_id', null=True)
    breakfast = models.ForeignKey(
        'recipe.Recipe', on_delete=models.SET_NULL, related_name='breakfast', null=True)
    snack = models.ForeignKey(
        'recipe.Recipe', on_delete=models.SET_NULL, related_name='snack', null=True)
    lunch = models.ForeignKey(
        'recipe.Recipe', on_delete=models.SET_NULL, related_name='lunch', null=True)
    teatime = models.ForeignKey(
        'recipe.Recipe', on_delete=models.SET_NULL, related_name='teatime', null=True)
    dinner = models.ForeignKey(
        'recipe.Recipe', on_delete=models.SET_NULL, related_name='dinner', null=True)

    def __str__(self):
        return self.day
