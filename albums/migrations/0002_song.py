# Generated by Django 4.1.2 on 2022-10-20 21:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('thumb', imagekit.models.fields.ProcessedImageField(upload_to='')),
                ('audio', models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['mp3', 'wav'])])),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.album')),
            ],
        ),
    ]
