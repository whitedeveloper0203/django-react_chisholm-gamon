# Generated by Django 2.0.8 on 2018-08-22 03:12

import chisholm.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20180822_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpagewithform',
            name='sidebar',
            field=wagtail.core.fields.StreamField([('panels', wagtail.core.blocks.StreamBlock([('latest_posts', wagtail.core.blocks.StructBlock([('number_of_articles', wagtail.core.blocks.IntegerBlock(default=3)), ('see_all_text', wagtail.core.blocks.CharBlock(help_text='Button text for "See all"', required=False)), ('see_all_link', wagtail.core.blocks.PageChooserBlock())])), ('find_it_fast', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='find it fast')), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('tagline', wagtail.core.blocks.CharBlock(required=False))])))])), ('image_link', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.PageChooserBlock())])), ('testimonials', wagtail.core.blocks.StructBlock([('testimonials', wagtail.core.blocks.ListBlock(wagtail.snippets.blocks.SnippetChooserBlock(target_model='testimonials.Testimonial')))])), ('offices', chisholm.blocks.OurOfficesBlock()), ('latest_properties', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Latest Properties')), ('property_type', wagtail.core.blocks.ChoiceBlock(choices=[])), ('limit', wagtail.core.blocks.IntegerBlock(default=3))])), ('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('secondary_link', wagtail.core.blocks.PageChooserBlock(help_text="Will show 2 CTA's side by side", required=False))]))], max_num=3))], default={}),
            preserve_default=False,
        ),
    ]
