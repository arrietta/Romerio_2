# Generated by Django 5.1.2 on 2024-10-22 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romerio', '0012_colors_additional_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bevels',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]