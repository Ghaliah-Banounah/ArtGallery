# Generated by Django 5.1.3 on 2024-11-26 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtPiece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('isSold', models.BooleanField(default=False)),
                ('currentLocation', models.CharField(max_length=1024)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='artists.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/default.jpg', upload_to='images/pieces/')),
                ('piece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artPieces.artpiece')),
            ],
        ),
    ]