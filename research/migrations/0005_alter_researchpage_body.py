# Generated by Django 4.2.2 on 2023-07-05 17:48

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0004_alter_researchpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='title')), ('paragraph', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.blocks.TextBlock(identifier='code', label='Code'))], label='Code'))], use_json_field=True),
        ),
    ]
