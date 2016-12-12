# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-30 01:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentas', '0014_auto_20161125_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=150)),
                ('fecha', models.DateField()),
                ('comentario', models.TextField()),
                ('renta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentas.Renta')),
            ],
        ),
        migrations.AlterField(
            model_name='galeria',
            name='renta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentas.Renta'),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='renta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentas.Renta'),
        ),
    ]