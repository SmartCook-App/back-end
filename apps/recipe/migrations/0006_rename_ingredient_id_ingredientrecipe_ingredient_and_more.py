# Generated by Django 4.0 on 2022-01-19 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_remove_lasttimecooked_lasttimecooked_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientrecipe',
            old_name='ingredient_id',
            new_name='ingredient',
        ),
        migrations.RenameField(
            model_name='ingredientrecipe',
            old_name='recipe_id',
            new_name='recipe',
        ),
        migrations.RenameField(
            model_name='lasttimecooked',
            old_name='recipe_id',
            new_name='recipe',
        ),
        migrations.RenameField(
            model_name='lasttimecooked',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='recipenotes',
            old_name='recipe_id',
            new_name='recipe',
        ),
        migrations.RenameField(
            model_name='recipenotes',
            old_name='user_id',
            new_name='user',
        ),
    ]