# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-15 02:02
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('realestate', '0003_listingenquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingSearchPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('canonical', models.URLField(blank=True, default='')),
                ('title_tag', models.CharField(blank=True, default='', max_length=255)),
                ('meta_title', models.CharField(blank=True, default='', max_length=255)),
                ('meta_description', models.TextField(blank=True, default='')),
                ('meta_keywords', models.TextField(blank=True, default='')),
                ('og_title', models.CharField(blank=True, default='', max_length=255)),
                ('og_type', models.CharField(blank=True, default='', max_length=50)),
                ('og_url', models.URLField(blank=True, default='')),
                ('og_img', models.URLField(blank=True, default='')),
                ('og_description', models.TextField(blank=True, default='')),
                ('twitter_card', models.CharField(blank=True, default='', help_text='Type of Twitter card', max_length=50)),
                ('twitter_site', models.CharField(blank=True, default='', help_text='@name of publisher', max_length=50)),
                ('twitter_title', models.CharField(blank=True, default='', max_length=255)),
                ('twitter_description', models.CharField(blank=True, default='', max_length=200)),
                ('twitter_creator', models.CharField(blank=True, default='', help_text='@name of author', max_length=50)),
                ('twitter_image', models.CharField(blank=True, default='', help_text='Images must be at least 120x120px', max_length=255)),
                ('template_override', models.CharField(blank=True, default='', help_text='Load this specific page template', max_length=255)),
                ('search_params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={})),
                ('description', wagtail.core.fields.RichTextField(blank=True, default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='SearchPageFeaturedListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.PropertyListing')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_listings', to='realestate.ListingSearchPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
