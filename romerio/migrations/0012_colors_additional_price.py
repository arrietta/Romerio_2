# Generated by Django 5.1.2 on 2024-10-22 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romerio', '0011_bevels'),
    ]

    operations = [
        migrations.AddField(
            model_name='colors',
            name='additional_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
