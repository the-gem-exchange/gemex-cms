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
	node_css = models.TextField(blank=True)

	type = models.CharField(
		choices=[
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
		layer = MapLocationImage.objects.filter(location=self).first()
		if layer and layer.image:
			return format_html(
				'<img class="species-thumbnail" src="{}" />',
				layer.image.file.url,
			)
		else:
			return None

	def _overlay(self):
		layers = MapLocationOverlay.objects.filter(location=self)
		if layers:
			html = '<div class="map-overlay-thumbnail">'
			for layer in layers:
				html += format_html(
					'<img style="max-width:300px; border: 1px solid #333;" src="{}" />',
					layer.image.file.url,
				)
			html += '</div>'
			return format_html(html)
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
			FieldPanel('node_css', classname="code-editor"),
			HelpPanel(content='Inline styles for this node.'),
		], heading="Code"),

		MultiFieldPanel([
			InlinePanel('node_image'),
			HelpPanel(content='Replace the dot with an image. Can be multiple layers.'),
		], heading="Node Replacement Image"),


		MultiFieldPanel([
			InlinePanel('overlay_image'),
			HelpPanel(content='Overlays for the entire map, activated on hover. Should match the resolution of the map image.'),
		], heading="Overlay Image"),
	]

	def save(self):
		# If code exists, overwrite existing coords
		if self.node_html:
			# Extract attrs from div
			soup  = BeautifulSoup(self.node_html+"</div>", 'html5lib')
			div   = soup.div
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


class MapLocationImage(Orderable):

	location = ParentalKey(MapLocation, on_delete=models.CASCADE, related_name='node_image')

	image  = models.ForeignKey(
 		'image.CustomImage',
 		null=True,
 		blank=True,
 		on_delete=models.SET_NULL,
 		related_name="node_image",
 	)

	panels = [
		ImageChooserPanel('image')
	]


class MapLocationOverlay(Orderable):

	location = ParentalKey(MapLocation, on_delete=models.CASCADE, related_name='overlay_image')

	image  = models.ForeignKey(
 		'image.CustomImage',
 		null=True,
 		blank=True,
 		on_delete=models.SET_NULL,
 		related_name="overlay_image",
 	)

	panels = [
		ImageChooserPanel('image')
	]


from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
class MapLocationAdmin(ModelAdmin):
	model         = MapLocation
	menu_icon     = 'site'
	list_display  = ('_image', '_title', 'type', '_description', '_overlay')
	search_fields = ['title', 'description', 'type']
	list_display_add_buttons = '_title'

modeladmin_register(MapLocationAdmin)
