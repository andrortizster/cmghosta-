# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-18 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentas', '0005_remove_renta_municipio'),
    ]

    operations = [
        migrations.AddField(
            model_name='renta',
            name='municipio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rentas.Municipio'),
            preserve_default=False,
        ),
    ]
