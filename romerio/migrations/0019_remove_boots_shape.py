# Generated by Django 5.1.2 on 2024-10-23 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('romerio', '0018_shape_has_grid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boots',
            name='Shape',
        ),
    ]