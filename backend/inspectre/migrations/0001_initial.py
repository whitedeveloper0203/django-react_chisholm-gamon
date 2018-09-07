# Generated by Django 2.0.3 on 2018-03-22 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='InspectRealEstateSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspect_real_estate_agentid', models.CharField(blank=True, default='', help_text='IRE agentID to integrate with their system', max_length=50)),
                ('inspect_real_estate_base_url', models.CharField(default='https://book.inspectrealestate.com.au/Register', max_length=255)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]