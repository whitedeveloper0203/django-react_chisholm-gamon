# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-07 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0005_auto_20180201_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonialagent',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='agents.AgentPage'),
        ),
    ]
