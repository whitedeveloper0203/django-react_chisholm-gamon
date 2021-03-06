# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('suburbs', '0002_auto_20180219_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuburbIndexFeaturedSuburb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('index', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_suburbs', to='suburbs.SuburbIndex')),
                ('suburb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suburbs.SuburbPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
