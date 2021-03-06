# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-26 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentas', '0013_auto_20161124_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrada', models.DateField(verbose_name='Fecha de entrada')),
                ('fecha_salida', models.DateField(verbose_name='Fecha de salida')),
                ('nombre_cliente', models.TextField(max_length=150, verbose_name='Nombre del cliente')),
                ('email_cliente', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('cantidad_personas', models.IntegerField(verbose_name='Cantidad de personas')),
                ('confirmado', models.BooleanField(default=False)),
                ('renta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentas.Renta')),
            ],
        ),
        migrations.AlterField(
            model_name='galeria',
            name='renta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentas.Renta'),
        ),
    ]
