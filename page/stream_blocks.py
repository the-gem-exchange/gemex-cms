from wagtail.core             import blocks
from wagtail.images.blocks    import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.snippets.blocks  import SnippetChooserBlock

class FullSizeImage(blocks.StructBlock):
	image = ImageChooserBlock(help_text="Full width, full height")

	class Meta:
		template = 'blocks/info_sheet.html'
		form_classname = "info-sheet"


class ColumnOptions(blocks.StructBlock):
	column_options = blocks.StructBlock([
		('classes', blocks.CharBlock(required=False, max_length=255, help_text="Apply custom classes to this column.")),
	])
	content = blocks.RichTextBlock(required=False, classname="column-content")

	class Meta:
		form_classname = "column-options"

class RowOptions(blocks.StructBlock):
	background_image = ImageChooserBlock(required=False)

	class Meta:
		form_classname = "row-options"


class OneColumn(blocks.StructBlock):
	row_options = RowOptions(required=False)

	column      = ColumnOptions(required=False, classname="field-one_column")

	def get_context(self, value, parent_context=None):
		context = super().get_context(value, parent_context=parent_context)
		context['background_image'] = value['row_options']['background_image']
		return context

	class Meta:
		template       = 'blocks/blocks_row.html'
		form_classname = 'columns one-column'

class TwoColumns(blocks.StructBlock):
	row_options  = RowOptions(required=False)

	left_column  = ColumnOptions(required=False, classname="field-two_columns_left")
	right_column = ColumnOptions(required=False, classname="field-two_columns_right")

	def get_context(self, value, parent_context=None):
		context = super().get_context(value, parent_context=parent_context)
		context['background_image'] = value['row_options']['background_image']
		return context

	class Meta:
		template       = 'blocks/blocks_row.html'
		form_classname = 'columns two-columns'

class ThreeColumns(blocks.StructBlock):
	row_options   = RowOptions(required=False)

	left_column   = ColumnOptions(required=False, classname="field-three_columns_left")
	center_column = ColumnOptions(required=False, classname="field-three_columns_center")
	right_column  = ColumnOptions(required=False, classname="field-three_columns_right")

	def get_context(self, value, parent_context=None):
		context = super().get_context(value, parent_context=parent_context)
		context['background_image'] = value['row_options']['background_image']
		return context

	class Meta:
		template       = 'blocks/blocks_row.html'
		form_classname = 'columns three-columns'


class HTMLBlock(blocks.StructBlock):
	html_content = blocks.TextBlock(classname="code-editor")

	class Meta:
		template = 'blocks/blocks_html.html'


stream_blocks = [
	('HTML',            HTMLBlock(icon='fa-code')),
	('One_Column',      OneColumn(icon='one-column')),
	('Two_Columns',     TwoColumns(icon='two-columns')),
	('Three_Columns',   ThreeColumns(icon='three-columns')),
	('Full_Size_Image', FullSizeImage(icon='form'))
]
