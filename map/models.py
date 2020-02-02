from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import InlinePanel, FieldPanel, MultiFieldPanel
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
	node_html   = models.TextField(
		blank=True,
	)
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

	def __str__(self):
		return self.title

	panels = [
		FieldPanel('title'),
		FieldPanel('description'),
		FieldPanel('node_html'),
		ImageChooserPanel('node_image'),
		ImageChooserPanel('overlay_image'),
	]

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
class MapLocationAdmin(ModelAdmin):
	model         = MapLocation
	menu_icon     = 'site'
	list_display  = ('title',)
	search_fields = ['title']
	list_display_add_buttons = 'title'

modeladmin_register(MapLocationAdmin)
