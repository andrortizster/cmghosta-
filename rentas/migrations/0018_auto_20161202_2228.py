# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-03 03:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentas', '0017_auto_20161202_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='renta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentas.Renta'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='renta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentas.Renta'),
        ),
        migrations.AlterField(
            model_name='renta',
            name='movil',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='renta',
            name='telefono',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='renta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentas.Renta'),
        ),
    ]
