# Generated by Django 4.1.2 on 2022-11-05 21:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='Cost',
            field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
