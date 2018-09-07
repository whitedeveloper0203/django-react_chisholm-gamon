# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-05 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0011_listingsearchpage_structured_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertylisting',
            name='status',
            field=models.CharField(choices=[('current', 'Current'), ('premarket', 'Pre-Market / Off market Sale'), ('withdrawn', 'Withdrawn'), ('offmarket', 'Off market: Not for Sale/Lease'), ('deleted', 'Deleted'), ('leased', 'Leased'), ('sold', 'Sold')], db_index=True, default='current', max_length=25),
        ),
    ]
