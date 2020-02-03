from bs4 import BeautifulSoup # Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from django.db import models
from django.utils.html import format_html

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

import re

from wagtail.admin.edit_handlers import InlinePanel, FieldPanel, HelpPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


@register_setting
class MapSettings(ClusterableModel, BaseSetting):

	map_image = models.ForeignKey(
		'image.CustomImage',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name="map_image"
	)

	panels = [
		MultiFieldPanel([
			ImageChooserPanel('map_image'),
		], heading="Jo'Arca Map Settings")
	]

@register_snippet
class MapLocation(index.Indexed, ClusterableModel):

	title       = models.CharField(max_length=255, help_text="The name as it appears on the map.")
	description = RichTextField(blank=True)

	node_id = models.CharField(blank=True, max_length=255)
	x = models.CharField(blank=True, max_length=255)
	y = models.CharField(blank=True, max_length=255)
	width  = models.CharField(blank=True, max_length=255)
	height = models.CharField(blank=True, max_length=255)
	rotate = models.CharField(blank=True, max_length=10, help_text="Rotates the icon/title on the map, in degrees (180, -45, 90, etc)")

	node_html = models.TextField(blank=True)

	node_image  = models.ForeignKey(
		'image.CustomImage',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name="node_image",
		help_text="Replaces the dot with an image."
	)
	overlay_image = models.ForeignKey(
		'image.CustomImage',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name="overlay_image",
		help_text="A transparent layer over the whole map that is related to this location."
	)

	type = models.CharField(
		choices=[
			('capitol',   'Capitol'),
			('continent', 'Continent'),
			('hidden',    'Hidden'),
			('ocean',     'Ocean'),
			('none',      'Not on map'),
			('standard',  'Standard'),
			('text',      'Text'),
			('turtle',    'Turtle'),
		],
		null=True,
		blank=False,
		default='standard',
		max_length=255
	)

	def __str__(self):
		return self.title

	def _title(self):
		return format_html(
			'<b style="min-width: 200px;">{}</b>',
			self.title
		)

	def _description(self):
		return format_html(
			'<div style="max-width:500px;">{}</div>',
			format_html(self.description)
		)

	def _image(self):
		if self.node_image:
			return format_html(
				'<img class="species-thumbnail" src="{}" />',
				self.node_image.file.url,
			)
		else:
			return None

	def _overlay(self):
		if self.overlay_image:
			return format_html(
				'<img style="max-width:300px; border: 1px solid #333;" src="{}" />',
				self.overlay_image.file.url,
			)
		else:
			return None

	panels = [
		FieldPanel('title'),
		FieldPanel('type'),
		FieldPanel('description'),

		MultiFieldPanel([
			FieldPanel('node_id'),
			FieldPanel('rotate'),
			FieldPanel('width'),
			FieldPanel('height'),
			FieldPanel('x'),
			FieldPanel('y'),
		], heading="Positioning"),

		MultiFieldPanel([
			FieldPanel('node_html', classname="code-editor"),
			HelpPanel(content='Paste HTML code here to overwrite settings. HTML can be generated <a target="_blank" href="https://www.inabrains.com/tooltip/image-hotspot-creator.html">here</a>.'),
		], heading="Code"),

		ImageChooserPanel('node_image'),
		ImageChooserPanel('overlay_image'),
	]

	def save(self):
		# If code exists, overwrite existing coords
		if self.node_html:
			# Extract attrs from div
			soup = BeautifulSoup(self.node_html+"</div>", 'html5lib')
			div  = soup.div
			attrs = div.attrs


			self.node_id = attrs.get('id', self.node_id)

			# Extract styles
			rx     = re.compile(r'(?:width|height|top|left):[^;]+;?')
			styles = rx.findall(self.node_html)

			# Assign found styles to fields
			for style in styles:
				if 'width' in style:
					self.width = style.replace(';','').replace('width:','').strip(' ')
				if 'height' in style:
					self.height = style.replace(';','').replace('height:','').strip(' ')
				if 'left' in style:
					self.x = style.replace(';','').replace('left:','').strip(' ')
				if 'top' in style:
					self.y = style.replace(';','').replace('top:','').strip(' ')

			self.node_html = ''

			super(MapLocation, self).save()


from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
class MapLocationAdmin(ModelAdmin):
	model         = MapLocation
	menu_icon     = 'site'
	list_display  = ('_image', '_title', 'type', '_description', '_overlay')
	search_fields = ['title', 'description', 'type']
	list_display_add_buttons = '_title'

modeladmin_register(MapLocationAdmin)
