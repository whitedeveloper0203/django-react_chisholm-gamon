# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-09 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171208_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='title_tag',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='title_tag',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
