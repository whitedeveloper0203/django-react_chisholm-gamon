# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-04 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suburbs_database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suburbdata',
            name='area',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
    ]
