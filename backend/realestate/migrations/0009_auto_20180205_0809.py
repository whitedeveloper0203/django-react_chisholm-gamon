# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-05 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0008_auto_20180201_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertylisting',
            name='property_class',
            field=models.CharField(choices=[('residential', 'Residential'), ('commercial', 'Commercial'), ('land', 'Land'), ('holidayRental', 'Holiday'), ('rural', 'Rural')], db_index=True, default='residential', max_length=25),
        ),
    ]
