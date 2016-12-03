# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-17 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='renta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('habitaciones', models.PositiveIntegerField()),
                ('aire', models.BooleanField()),
                ('tv', models.BooleanField()),
                ('taxi', models.BooleanField()),
                ('refrigerador', models.BooleanField()),
                ('desayunos', models.BooleanField()),
                ('comidas', models.BooleanField()),
            ],
        ),
    ]
