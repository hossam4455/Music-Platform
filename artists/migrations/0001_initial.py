# Generated by Django 4.1.2 on 2022-11-10 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Artist_name', models.CharField(max_length=200, unique=True)),
                ('Artist_link', models.URLField(blank=True)),
            ],
        ),
    ]
