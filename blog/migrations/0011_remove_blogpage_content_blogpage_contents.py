# Generated by Django 4.2.2 on 2023-07-05 20:50

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blogpage_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='content',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='contents',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='title')), ('paragraph', wagtail.blocks.TextBlock(blank=True)), ('embed', wagtail.embeds.blocks.EmbedBlock(blank=True)), ('link', wagtail.blocks.URLBlock(blank=True))], blank=True, use_json_field=True),
        ),
    ]
