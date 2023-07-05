# Generated by Django 4.2.2 on 2023-07-05 20:45

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='title')), ('paragraph', wagtail.blocks.TextBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('link', wagtail.blocks.URLBlock())], blank=True, use_json_field=True),
        ),
    ]