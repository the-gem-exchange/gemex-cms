from django.db import models
from django.utils.html import format_html

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

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

	node_html = models.TextField(blank=True)
	rotate    = models.CharField(blank=True, max_length=10, help_text="Rotates the icon/title on the map, in degrees (180, -45, 90, etc)")

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
		FieldPanel('rotate'),

		FieldPanel('node_html', classname="code-editor"),
		HelpPanel(content='HTML can be generated <a target="_blank" href="https://www.inabrains.com/tooltip/image-hotspot-creator.html">here</a>'),

		ImageChooserPanel('node_image'),
		ImageChooserPanel('overlay_image'),
	]

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
class MapLocationAdmin(ModelAdmin):
	model         = MapLocation
	menu_icon     = 'site'
	list_display  = ('_image', '_title', 'type', '_description', '_overlay')
	search_fields = ['title', 'description', 'type']
	list_display_add_buttons = '_title'

modeladmin_register(MapLocationAdmin)
