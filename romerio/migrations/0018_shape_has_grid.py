# Generated by Django 5.1.2 on 2024-10-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romerio', '0017_grid'),
    ]

    operations = [
        migrations.AddField(
            model_name='shape',
            name='has_grid',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
