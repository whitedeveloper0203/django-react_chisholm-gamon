# Generated by Django 2.0.3 on 2018-04-05 22:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('suburbs', '0004_auto_20180301_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuburbPageDwellingStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('dwelling_type', models.CharField(max_length=255)),
                ('percentage', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='suburbpage',
            name='average_beds',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4),
        ),
        migrations.AddField(
            model_name='suburbpage',
            name='household_income',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='suburbpage',
            name='median_age',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4),
        ),
        migrations.AddField(
            model_name='suburbpage',
            name='mortgage_repayments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='suburbpage',
            name='population',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='suburbpagedwellingstats',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='dwelling_demos', to='suburbs.SuburbPage'),
        ),
    ]
