from django.db import models

from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import InlinePanel, FieldPanel
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.search import index
from wagtail.snippets.models import register_snippet


@register_snippet
class Stardragon(index.Indexed, ClusterableModel):

	name = models.CharField(max_length=255)

	# --- TO DO ---
	# rarity
	# species - list populated by snippets
	# traits list - list populated by snippets
	# Payment info - invoice #, transaction ID, Payment status, token used
	# owner (Name, Email)
	# color palette
	# images
	# links
	# description

	panels = [
		FieldPanel('name', classname="full title"),
	]

	def __str__(self):
		return self.name


class StardragonAdmin(ModelAdmin):
	model = Stardragon
	menu_icon = 'user'
	list_display = ('name')
	search_fields = ['name']

modeladmin_register(StardragonAdmin)
