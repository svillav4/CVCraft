# Generated by Django 5.0.7 on 2024-10-02 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0003_profile_tecnical_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='PhoneNumber',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
