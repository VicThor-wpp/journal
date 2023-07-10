# Generated by Django 4.2.2 on 2023-07-10 19:22

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_blogpage_contents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='contents',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='title')), ('paragraph', wagtail.blocks.TextBlock(blank=True)), ('embed', wagtail.embeds.blocks.EmbedBlock(blank=True, max_height=400, max_width=800)), ('link', wagtail.blocks.URLBlock(blank=True))], blank=True, use_json_field=True),
        ),
    ]
