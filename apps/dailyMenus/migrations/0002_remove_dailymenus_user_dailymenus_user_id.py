# Generated by Django 4.0 on 2022-01-12 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_follows_user'),
        ('dailyMenus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailymenus',
            name='user',
        ),
        migrations.AddField(
            model_name='dailymenus',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='user.user'),
        ),
    ]
