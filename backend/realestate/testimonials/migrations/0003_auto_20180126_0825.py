# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-26 08:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_auto_20180108_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonialoffice',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='offices.OfficePage'),
        ),
    ]
