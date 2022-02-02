# Generated by Django 4.0 on 2022-01-19 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_remove_lasttimecooked_lasttimecooked_and_more'),
        ('dailyMenus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailymenus',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='dailymenus',
            name='tetime',
        ),
        migrations.AddField(
            model_name='dailymenus',
            name='teatime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teatime', to='recipe.recipe'),
        ),
    ]
