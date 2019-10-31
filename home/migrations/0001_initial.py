# Generated by Django 2.2.6 on 2019-10-31 02:29

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.core.fields.StreamField([('Title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=255, required=False))], icon='title')), ('Subtitle', wagtail.core.blocks.StructBlock([('subtitle', wagtail.core.blocks.CharBlock(max_length=255, required=False))], icon='title')), ('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('One_Column', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.StructBlock([('colspan', wagtail.core.blocks.IntegerBlock(classname='column-options', help_text='Enter a value between 1 and 12. Defaults to auto.', max_value=12, min_value=1, required=False)), ('content', wagtail.core.blocks.RichTextBlock(classname='column-content', required=False))], classname='field-one_column', required=False)), ('row_options', wagtail.core.blocks.StructBlock([], required=False))], icon='one-column')), ('Two_Columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StructBlock([('colspan', wagtail.core.blocks.IntegerBlock(classname='column-options', help_text='Enter a value between 1 and 12. Defaults to auto.', max_value=12, min_value=1, required=False)), ('content', wagtail.core.blocks.RichTextBlock(classname='column-content', required=False))], classname='field-two_columns_left', required=False)), ('right_column', wagtail.core.blocks.StructBlock([('colspan', wagtail.core.blocks.IntegerBlock(classname='column-options', help_text='Enter a value between 1 and 12. Defaults to auto.', max_value=12, min_value=1, required=False)), ('content', wagtail.core.blocks.RichTextBlock(classname='column-content', required=False))], classname='field-two_columns_right', required=False)), ('row_options', wagtail.core.blocks.StructBlock([], required=False))], icon='two-columns')), ('Three_Columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StructBlock([('colspan', wagtail.core.blocks.IntegerBlock(classname='column-options', help_text='Enter a value between 1 and 12. Defaults to auto.', max_value=12, min_value=1, required=False)), ('content', wagtail.core.blocks.RichTextBlock(classname='column-content', required=False))], classname='field-three_columns_left', required=False)), ('center_column', wagtail.core.blocks.StructBlock([('colspan', wagtail.core.blocks.IntegerBlock(classname='column-options', help_text='Enter a value between 1 and 12. Defaults to auto.', max_value=12, min_value=1, required=False)), ('content', wagtail.core.blocks.RichTextBlock(classname='column-content', required=False))], classname='field-three_columns_center', required=False)), ('right_column', wagtail.core.blocks.StructBlock([('colspan', wagtail.core.blocks.IntegerBlock(classname='column-options', help_text='Enter a value between 1 and 12. Defaults to auto.', max_value=12, min_value=1, required=False)), ('content', wagtail.core.blocks.RichTextBlock(classname='column-content', required=False))], classname='field-three_columns_right', required=False)), ('row_options', wagtail.core.blocks.StructBlock([], required=False))], icon='three-columns'))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
