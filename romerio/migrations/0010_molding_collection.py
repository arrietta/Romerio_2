# Generated by Django 5.1.2 on 2024-10-22 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romerio', '0009_alter_shape_bevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='molding',
            name='collection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='romerio.collection'),
        ),
    ]