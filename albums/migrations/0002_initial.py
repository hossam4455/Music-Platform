# Generated by Django 4.1.2 on 2022-11-12 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='Artist_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_album', to='artists.artists'),
        ),
    ]
