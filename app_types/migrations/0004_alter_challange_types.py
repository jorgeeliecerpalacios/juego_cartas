# Generated by Django 5.0.6 on 2024-09-15 00:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_types', '0003_alter_type_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challange',
            name='types',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='challange', to='app_types.type'),
        ),
    ]
