# Generated by Django 5.0.7 on 2024-10-01 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0002_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tecnical_information',
            field=models.TextField(blank=True, null=True),
        ),
    ]
