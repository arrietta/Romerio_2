# Generated by Django 5.1.2 on 2024-10-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romerio', '0015_bevels_icon_boots_icon_colors_hex_cornice_icon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shape',
            name='glass',
            field=models.ImageField(default='none', upload_to='glass/'),
        ),
    ]
