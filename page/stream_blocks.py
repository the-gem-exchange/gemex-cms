from wagtail.core import blocks
from wagtail.images.blocks    import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.snippets.blocks  import SnippetChooserBlock

class ColumnOptions(blocks.StructBlock):
    colspan = blocks.IntegerBlock(required=False, classname="column-options", max_value=12, min_value=1, help_text="Enter a value between 1 and 12. Defaults to auto.")
    content = blocks.RichTextBlock(required=False, classname="column-content")
    class Meta:
        form_classname = "column-options"

class RowOptions(blocks.StructBlock):
    class Meta:
        form_classname = "row-options"

class SectionTitle(blocks.StructBlock):
    title = blocks.CharBlock(required=False, max_length=255)
    class Meta:
        template = 'blocks/blocks_title.html'

class SubTitle(blocks.StructBlock):
    subtitle = blocks.CharBlock(required=False, max_length=255)
    class Meta:
        template = 'blocks/blocks_subtitle.html'

class OneColumn(blocks.StructBlock):
    column      = ColumnOptions(required=False, classname="field-one_column")
    row_options = RowOptions(required=False)
    class Meta:
        template       = 'blocks/blocks_row.html'
        form_classname = 'columns one-column'

class TwoColumns(blocks.StructBlock):
    left_column  = ColumnOptions(required=False, classname="field-two_columns_left")
    right_column = ColumnOptions(required=False, classname="field-two_columns_right")
    row_options  = RowOptions(required=False)
    class Meta:
        template       = 'blocks/blocks_row.html'
        form_classname = 'columns two-columns'

class ThreeColumns(blocks.StructBlock):
    left_column   = ColumnOptions(required=False, classname="field-three_columns_left")
    center_column = ColumnOptions(required=False, classname="field-three_columns_center")
    right_column  = ColumnOptions(required=False, classname="field-three_columns_right")
    row_options   = RowOptions(required=False)
    class Meta:
        template       = 'blocks/blocks_row.html'
        form_classname = 'columns three-columns'

stream_blocks = [
    ('Title',         SectionTitle(icon='title')),
    ('Subtitle',      SubTitle(icon='title')),
    ('heading',       blocks.CharBlock(classname="full title")),
    ('paragraph',     blocks.RichTextBlock()),
    ('image',         ImageChooserBlock()),
    ('One_Column',    OneColumn(icon='one-column')),
    ('Two_Columns',   TwoColumns(icon='two-columns')),
    ('Three_Columns', ThreeColumns(icon='three-columns')),
]
