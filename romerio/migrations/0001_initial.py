# Generated by Django 5.1.2 on 2024-10-22 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('door_type', models.CharField(choices=[('DO', 'DO'), ('Classic', 'Classic')], max_length=7)),
                ('has_molding', models.BooleanField(default=False)),
                ('has_groove', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='forms/')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romerio.collection')),
            ],
        ),
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='casings/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romerio.shape')),
            ],
        ),
        migrations.CreateModel(
            name='Podium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='podiums/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romerio.shape')),
            ],
        ),
        migrations.CreateModel(
            name='Molding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='moldings/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('Shape', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='romerio.shape')),
            ],
        ),
        migrations.CreateModel(
            name='Cornice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='cornices/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romerio.shape')),
            ],
        ),
        migrations.CreateModel(
            name='Boots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='baseboards/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romerio.shape')),
            ],
        ),
        migrations.CreateModel(
            name='Socket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='sockets/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romerio.shape')),
            ],
        ),
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_type', models.CharField(choices=[('Enamel', 'Эмаль'), ('Veneer', 'Шпон')], max_length=7)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('Boots', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romerio.boots')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romerio.collection')),
                ('cornice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romerio.cornice')),
                ('podium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romerio.podium')),
                ('casing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romerio.portal')),
                ('Shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romerio.shape')),
                ('socket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romerio.socket')),
            ],
        ),
    ]
