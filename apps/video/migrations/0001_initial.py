# Generated by Django 4.0 on 2022-01-17 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe', '0003_lasttimecooked_recipenotes_recipe_difficulty_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField(max_length=200)),
                ('recipe_id_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_id_video', to='recipe.recipe')),
            ],
        ),
    ]
