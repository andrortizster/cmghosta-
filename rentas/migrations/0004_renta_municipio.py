# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-18 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentas', '0003_auto_20161118_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='renta',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentas.Municipio'),
            preserve_default=False,
        ),
    ]
