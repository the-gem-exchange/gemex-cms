# Generated by Django 2.2.6 on 2019-11-13 00:00

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpage',
            name='content',
            field=wagtail.core.fields.StreamField([('Title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=255, required=False))], icon='title')), ('Subtitle', wagtail.core.blocks.StructBlock([('subtitle', wagtail.core.blocks.CharBlock(max_length=255, required=False))], icon='title')), ('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('One_Column', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.StructBlock([('column_options', wagtail.core.blocks.StructBlock([('colspan', wagtail.core.blocks.CharBlock(help_text="Enter a number between 1 and 12, or 'auto'.", max_length=255, required=False)), ('classes', wagtail.core.blocks.CharBlock(help_text='Apply custom classes to this column.', max_length=255, required=False))])), ('content', wagtail.core.blocks.RichTextBlock(classname='column-content', required=False))], classname='field-one_column', required=False)), ('row_options', wagtail.core.blocks.StructBlock([], required=False))], icon='one-column')), ('Two_Columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StructBlock([('column_options', wagtail.core.blocks.StructBlock([('colspan', wagtail.core.blocks.CharBlock(help_text="Enter a number between 1 and 12, or 'auto'.", max_length=255, required=False)), ('classes', wagtail.core.blocks.CharBlock(help_text='Apply custom classes to this column.', max_length=255, required=False))])), ('content', wagtail.core.blocks.RichTextBlock(classname='column-content', required=False))], classname='field-two_columns_left', required=False)), ('right_column', wagtail.core.blocks.StructBlock([('column_options', wagtail.core.blocks.StructBlock([('colspan', wagtail.core.blocks.CharBlock(help_text="Enter a number between 1 and 12, or 'auto'.", max_length=255, required=False)), ('classes', wagtail.core.blocks.CharBlock(help_text='Apply custom classes to this column.', max_length=255, required=False))])), ('content', wagtail.core.blocks.RichTextBlock(classname='column-content', required=False))], classname='field-two_columns_right', required=False)), ('row_options', wagtail.core.blocks.StructBlock([], required=False))], icon='two-columns')), ('Three_Columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StructBlock([('column_options', wagtail.core.blocks.StructBlock([('colspan', wagtail.core.blocks.CharBlock(help_text="Enter a number between 1 and 12, or 'auto'.", max_length=255, required=False)), ('classes', wagtail.core.blocks.CharBlock(help_text='Apply custom classes to this column.', max_length=255, required=False))])), ('content', wagtail.core.blocks.RichTextBlock(classname='column-content', required=False))], classname='field-three_columns_left', required=False)), ('center_column', wagtail.core.blocks.StructBlock([('column_options', wagtail.core.blocks.StructBlock([('colspan', wagtail.core.blocks.CharBlock(help_text="Enter a number between 1 and 12, or 'auto'.", max_length=255, required=False)), ('classes', wagtail.core.blocks.CharBlock(help_text='Apply custom classes to this column.', max_length=255, required=False))])), ('content', wagtail.core.blocks.RichTextBlock(classname='column-content', required=False))], classname='field-three_columns_center', required=False)), ('right_column', wagtail.core.blocks.StructBlock([('column_options', wagtail.core.blocks.StructBlock([('colspan', wagtail.core.blocks.CharBlock(help_text="Enter a number between 1 and 12, or 'auto'.", max_length=255, required=False)), ('classes', wagtail.core.blocks.CharBlock(help_text='Apply custom classes to this column.', max_length=255, required=False))])), ('content', wagtail.core.blocks.RichTextBlock(classname='column-content', required=False))], classname='field-three_columns_right', required=False)), ('row_options', wagtail.core.blocks.StructBlock([], required=False))], icon='three-columns'))], blank=True),
        ),
    ]