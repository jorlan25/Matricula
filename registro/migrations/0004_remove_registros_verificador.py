# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-20 22:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_registros'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registros',
            name='verificador',
        ),
    ]
