# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-20 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='cupos',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='materia',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]
