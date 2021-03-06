# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-08 00:27
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import modelcluster.fields
import realestate.listings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('agents', '0002_agentpage_source_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspection_time', models.DateTimeField()),
                ('inspection_end_time', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ListingAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_agent', to='agents.AgentPage')),
            ],
        ),
        migrations.CreateModel(
            name='ListingFloorplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('floorplan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListingLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_type', models.CharField(choices=[('external', 'External'), ('video', 'Video'), ('vtour', 'Vtour'), ('soi', 'Statement of Information'), ('miniweb', 'Miniweb'), ('360tour', '360 Tour')], max_length=255)),
                ('href', models.URLField()),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListingVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(choices=[('commercial', [('Commercial Farming', 'Commercial Farming'), ('Land/Development', 'Land/Development'), ('Hotel/Leisure', 'Hotel/Leisure'), ('Industrial/Warehouse', 'Industrial/Warehouse'), ('Medical/Consulting', 'Medical/Consulting'), ('Offices', 'Offices'), ('Retail', 'Retail'), ('Showrooms/Bulky Goods', 'Showrooms/Bulky Goods'), ('Other', 'Other')]), ('residential', [('House', 'House'), ('Unit', 'Unit'), ('Townhouse', 'Townhouse'), ('Villa', 'Villa'), ('Apartment', 'Apartment'), ('Flat', 'Flat'), ('Studio', 'Studio'), ('Warehouse', 'Warehouse'), ('DuplexSemi-detached', 'DuplexSemi-detached'), ('Alpine', 'Alpine'), ('AcreageSemi-rural', 'AcreageSemi-rural'), ('Retirement', 'Retirement'), ('BlockOfUnits', 'BlockOfUnits'), ('Terrace', 'Terrace'), ('ServicedApartment', 'ServicedApartment'), ('Other', 'Other')]), ('holidayRental', [('Alpine', 'Alpine'), ('Unit', 'Unit'), ('ServicedApartment', 'ServicedApartment'), ('House', 'House'), ('Terrace', 'Terrace'), ('Flat', 'Flat'), ('Studio', 'Studio'), ('Villa', 'Villa'), ('Townhouse', 'Townhouse'), ('Apartment', 'Apartment'), ('DuplexSemi', 'DuplexSemi'), ('Retreat', 'Retreat'), ('BackpackerHostel', 'BackpackerHostel'), ('Campground', 'Campground'), ('CaravanHolidayPark', 'CaravanHolidayPark'), ('FarmStay', 'FarmStay'), ('HouseBoat', 'HouseBoat'), ('Hotel', 'Hotel'), ('Motel', 'Motel'), ('Lodge', 'Lodge'), ('ExecutiveRental', 'ExecutiveRental'), ('BedAndBreakfast', 'BedAndBreakfast'), ('Resort', 'Resort'), ('SelfContainedCottage', 'SelfContainedCottage'), ('Other', 'Other')]), ('rural', [('Cropping', 'Cropping'), ('Dairy', 'Dairy'), ('Farmlet', 'Farmlet'), ('Horticulture', 'Horticulture'), ('Livestock', 'Livestock'), ('Viticulture', 'Viticulture'), ('MixedFarming', 'MixedFarming'), ('Lifestyle', 'Lifestyle'), ('Other', 'Other')])], db_index=True, max_length=100)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertyFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('value', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertyListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agentID', models.CharField(help_text="The Office's Source ID", max_length=10, verbose_name='Agent ID')),
                ('uniqueID', models.CharField(help_text='Unique ID of the listing', max_length=255, verbose_name='Unique ID')),
                ('status', models.CharField(choices=[('current', 'Current'), ('withdrawn', 'Withdrawn'), ('offmarket', 'Offmarket'), ('deleted', 'Deleted'), ('leased', 'Leased'), ('sold', 'Sold')], db_index=True, default='current', max_length=25)),
                ('property_class', models.CharField(choices=[('commercial', 'Commercial'), ('land', 'Land'), ('residential', 'Residential'), ('holidayRental', 'Holiday'), ('rural', 'Rural')], db_index=True, default='residential', max_length=25)),
                ('listing_type', models.CharField(choices=[('sale', 'Sale'), ('lease', 'Lease'), ('both', 'Both')], db_index=True, default='sale', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('modTime', realestate.listings.models.REAXMLDateTimeField(blank=True, default=None, null=True)),
                ('priceView', models.CharField(blank=True, default='', max_length=255)),
                ('address_site', models.CharField(blank=True, default='', max_length=100, verbose_name='Site')),
                ('address_subNumber', models.CharField(blank=True, default='', max_length=100, verbose_name='Unit Number')),
                ('address_lotNumber', models.CharField(blank=True, default='', max_length=100, verbose_name='Lot Number')),
                ('address_streetNumber', models.CharField(blank=True, default='', max_length=100, verbose_name='Street Number')),
                ('address_street', models.CharField(blank=True, default='', max_length=100, verbose_name='Street Name')),
                ('address_suburb', models.CharField(blank=True, db_index=True, default='', max_length=100, verbose_name='Suburb')),
                ('address_state', models.CharField(blank=True, default='', max_length=100, verbose_name='State')),
                ('address_postcode', models.CharField(blank=True, db_index=True, default='', max_length=100, verbose_name='Postcode')),
                ('address_region', models.CharField(blank=True, default='', max_length=100, verbose_name='Region')),
                ('address_country', models.CharField(blank=True, default='Australia', max_length=100, verbose_name='Country')),
                ('address_display', realestate.listings.models.REAXMLBoolean(default=True, verbose_name='Show Address')),
                ('address_streetview', realestate.listings.models.REAXMLBoolean(default=True, verbose_name='Show Street View')),
                ('address_latitude', models.DecimalField(decimal_places=6, default=0.0, max_digits=9, null=True, verbose_name='Latitude')),
                ('address_longitude', models.DecimalField(decimal_places=6, default=0.0, max_digits=9, null=True, verbose_name='Longitdue')),
                ('municipality', models.CharField(blank=True, default='', max_length=255)),
                ('streetDirectory', models.CharField(blank=True, default='', max_length=255)),
                ('headline', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('buildingDetails_area', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True)),
                ('buildingDetails_area_unit', models.CharField(blank=True, default='', max_length=15)),
                ('buildingDetails_area_range_min', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True)),
                ('buildingDetails_area_range_max', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True)),
                ('buildingDetails_energyRating', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True)),
                ('buildingDetails_newlyBuilt', realestate.listings.models.REAXMLBoolean(default=False)),
                ('price', models.IntegerField(blank=True, db_index=True, default=0, null=True)),
                ('price_range_min', models.IntegerField(blank=True, default=0, verbose_name='Search price from')),
                ('price_range_max', models.IntegerField(blank=True, default=0, verbose_name='Search price to')),
                ('price_display', realestate.listings.models.REAXMLBoolean(default=True)),
                ('salebySetDate', realestate.listings.models.REAXMLDateTimeField(blank=True, default=None, null=True)),
                ('setSale_date', realestate.listings.models.REAXMLDateTimeField(blank=True, default=None, null=True)),
                ('soldDetails_price', models.IntegerField(blank=True, default=None, null=True)),
                ('soldDetails_price_display', realestate.listings.models.REAXMLBoolean(default=True)),
                ('soldDetails_date', realestate.listings.models.REAXMLDateTimeField(blank=True, default=None, null=True)),
                ('underOffer', realestate.listings.models.REAXMLBoolean(default=False, verbose_name='Under Offer?')),
                ('authority', models.CharField(default='sale', max_length=15)),
                ('authority_date', realestate.listings.models.REAXMLDateTimeField(blank=True, default=None, null=True)),
                ('auction_date', realestate.listings.models.REAXMLDateTimeField(blank=True, default=None, null=True)),
                ('rent', models.IntegerField(db_index=True)),
                ('rent_period', models.CharField(choices=[('week', 'Week'), ('weekly', 'Weekly'), ('month', 'Month'), ('monthly', 'Monthly')], default='week', max_length=10)),
                ('rent_display', realestate.listings.models.REAXMLBoolean(default=True)),
                ('bond', realestate.listings.models.CurrencyIntegerField(blank=True, default=None, null=True)),
                ('dateAvailable', realestate.listings.models.REAXMLDateTimeField(blank=True, default=None, null=True)),
                ('isHomeLandPackage', realestate.listings.models.REAXMLBoolean(default=False)),
                ('holiday', realestate.listings.models.REAXMLBoolean(default=False)),
                ('newConstruction', realestate.listings.models.REAXMLBoolean(default=False)),
                ('project_id', models.CharField(blank=True, default='', max_length=50)),
                ('estate_name', models.CharField(blank=True, default='', max_length=255)),
                ('estate_stage', models.CharField(blank=True, default='', max_length=255)),
                ('commercialAuthority_value', models.CharField(choices=[('auction', 'Auction'), ('tender', 'Tender'), ('eoi', 'Eoi'), ('sale', 'Sale'), ('forsale', 'Forsale'), ('offers', 'Offers')], default='sale', max_length=10)),
                ('exclusivity_value', models.CharField(choices=[('exclusive', 'Exclusive'), ('open', 'Open')], default='exclusive', max_length=10)),
                ('commercialRent', models.IntegerField(default=0)),
                ('commercialRent_plusOutgoings', realestate.listings.models.REAXMLBoolean(default=False)),
                ('commercialRent_tax', models.CharField(choices=[('unknown', 'Unknown'), ('exempt', 'Exempt'), ('inclusive', 'Inclusive'), ('exclusive', 'Exclusive')], default='unknown', max_length=10)),
                ('outgoings', models.IntegerField(default=0)),
                ('_return', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('currentLeaseEndDate', models.DateField(blank=True, default=None, null=True)),
                ('tenancy', models.CharField(choices=[('unknown', 'Unknown'), ('vacant', 'Vacant'), ('tenanted', 'Tenanted')], default='unknown', max_length=10)),
                ('furtherOptions', models.TextField(blank=True, default='')),
                ('isMultiple', realestate.listings.models.REAXMLBoolean(default=False)),
                ('propertyExtent', models.CharField(blank=True, choices=[('whole', 'Whole'), ('part', 'Part')], default='', max_length=10)),
                ('carSpaces', models.IntegerField(default=0)),
                ('parkingComments', models.CharField(blank=True, default='', max_length=255)),
                ('zone', models.CharField(blank=True, default='', max_length=255)),
                ('address_suburb_display', realestate.listings.models.REAXMLBoolean(default=True)),
                ('area', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True)),
                ('area_unit', models.CharField(blank=True, default='', max_length=15)),
                ('area_range_min', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True)),
                ('area_range_max', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True)),
                ('frontage', models.CharField(blank=True, default='', max_length=255)),
                ('frontage_unit', models.CharField(blank=True, default='', max_length=15)),
                ('depth', models.CharField(blank=True, default='', max_length=255)),
                ('depth_unit', models.CharField(blank=True, default='', max_length=15)),
                ('depth_side', models.CharField(blank=True, default='', max_length=10)),
                ('crossOver_value', models.CharField(blank=True, default='', max_length=10)),
                ('extraFields', django.contrib.postgres.fields.jsonb.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('telephone_bh', models.CharField(blank=True, max_length=50)),
                ('telephone_mobile', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='propertylisting',
            unique_together=set([('agentID', 'uniqueID')]),
        ),
        migrations.AddField(
            model_name='propertyfeature',
            name='listing',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='realestate.PropertyListing'),
        ),
        migrations.AddField(
            model_name='propertycategory',
            name='listing',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='realestate.PropertyListing'),
        ),
        migrations.AddField(
            model_name='listingvendor',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.Vendor'),
        ),
        migrations.AddField(
            model_name='listinglink',
            name='listing',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='hrefs', to='realestate.PropertyListing'),
        ),
        migrations.AddField(
            model_name='listingimage',
            name='listing',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='realestate.PropertyListing'),
        ),
        migrations.AddField(
            model_name='listingfloorplan',
            name='listing',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='floorplans', to='realestate.PropertyListing'),
        ),
        migrations.AddField(
            model_name='listingagent',
            name='listing',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents', to='realestate.PropertyListing'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='listing',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspections', to='realestate.PropertyListing'),
        ),
        migrations.AlterUniqueTogether(
            name='listingagent',
            unique_together=set([('agent', 'listing')]),
        ),
    ]
