# Generated by Django 3.0 on 2022-10-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0005_auto_20221006_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='Link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='artists',
            name='Name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
