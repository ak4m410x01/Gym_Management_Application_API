# Generated by Django 5.0.1 on 2024-02-06 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='coachsalary',
            unique_together={('coach', 'salary')},
        ),
    ]
