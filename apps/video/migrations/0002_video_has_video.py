# Generated by Django 4.0 on 2022-01-19 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='has_video',
            field=models.BooleanField(default=False),
        ),
    ]
