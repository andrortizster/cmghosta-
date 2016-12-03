# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-18 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentas', '0002_renta'),
    ]

    operations = [
        migrations.AddField(
            model_name='renta',
            name='descripcion',
            field=models.TextField(default='Escriba la descripci\xf3n del inmueble', verbose_name='Descripci\xf3n'),
        ),
        migrations.AddField(
            model_name='renta',
            name='description',
            field=models.TextField(default='Enter property description', verbose_name='Descripci\xf3n en Ingles'),
        ),
        migrations.AddField(
            model_name='renta',
            name='descrizione',
            field=models.TextField(default='Digitare la descrizione della propriet\xe0', verbose_name='Descripci\xf3n en Italiano'),
        ),
    ]
