# Generated by Django 3.0 on 2022-10-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='artists',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]