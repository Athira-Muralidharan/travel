# Generated by Django 4.1.7 on 2023-04-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0006_alter_team_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='pics1'),
        ),
    ]
