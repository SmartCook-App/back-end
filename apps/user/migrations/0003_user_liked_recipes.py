# Generated by Django 4.0 on 2022-01-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_initial'),
        ('user', '0002_user_follows_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='liked_recipes',
            field=models.ManyToManyField(related_name='liked_recipes', to='recipe.Recipe'),
        ),
    ]