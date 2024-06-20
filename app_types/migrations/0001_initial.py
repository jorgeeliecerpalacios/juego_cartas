# Generated by Django 5.0.6 on 2024-06-19 23:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('baraja', 'Naipes'), ('cartas', 'Uno'), ('tarjetas', 'Golpe')], max_length=255)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='types/photos')),
                ('quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]