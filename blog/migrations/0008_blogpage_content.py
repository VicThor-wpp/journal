# Generated by Django 4.2.2 on 2023-07-05 20:28

from django.db import migrations
import django.utils.timezone
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpage_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='content',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='title')), ('paragraph', wagtail.blocks.TextBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('link', wagtail.blocks.URLBlock())], default=django.utils.timezone.now, use_json_field=True),
            preserve_default=False,
        ),
    ]
