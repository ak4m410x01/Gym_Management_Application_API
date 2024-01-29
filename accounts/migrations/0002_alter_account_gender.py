# Generated by Django 5.0.1 on 2024-01-29 18:18

import accounts.validators.gender
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(max_length=1, validators=[accounts.validators.gender.genderValidator]),
        ),
    ]
