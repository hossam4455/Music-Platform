# Generated by Django 4.1.2 on 2022-10-23 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_auto_20221021_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
