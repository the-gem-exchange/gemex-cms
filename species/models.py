from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from trait.models import Trait

from wagtail.admin.edit_handlers import InlinePanel, FieldPanel
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


@register_snippet
class Species(index.Indexed, ClusterableModel):

	name  = models.CharField(max_length=255)
	color = models.CharField(max_length=255, blank=True)

	panels = [
		FieldPanel('name', classname='full title'),
		FieldPanel('color'),
		InlinePanel('subspecies', label="Subspecies"),
	]

	def description(self):
		return self.subspecies.get(name="Standard").description

	def background(self):
		return self.subspecies.get(name="Standard").background

	def thumbnail(self):
		return self.subspecies.get(name="Standard").thumbnail()

	def subspecies_(self):
		return ', '.join(x.name for x in self.subspecies.all())

	def traits(self):
		traits = Trait.objects.filter(species__species=self)
		return traits

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["name"]
		verbose_name_plural = "Species"


class SubSpecies(Orderable):
	species     = ParentalKey(Species, on_delete=models.CASCADE, related_name='subspecies')
	name        = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	image       = models.ForeignKey('image.CustomImage',  null=True, blank=True,  on_delete=models.SET_NULL, related_name="species_image")
	background  = models.ForeignKey('image.CustomImage',  null=True, blank=True,  on_delete=models.SET_NULL, related_name="species_background")

	panels = [
		FieldPanel('name'),
		FieldPanel('description'),
		ImageChooserPanel('image'),
		ImageChooserPanel('background'),
	]

	api_fields = [
		'name',
		'species'
	]

	def color(self):
		return self.species.color

	def traits(self):
		return Trait.objects.filter(species=self)

	def thumbnail(self):
		if(self.image):
			return format_html(
				'<img class="species-thumbnail" src="{}" />',
				self.image.file.url,
			)
		else:
			return self.species.thumbnail()

	def subspecies(self):
		return self.name

	def __str__(self):
		return self.species.name + " ("+self.name+")"


class SpeciesAdmin(ModelAdmin):
	model         = Species
	menu_icon     = 'group'
	list_display  = ('thumbnail', 'name', 'subspecies_')
	search_fields = ['name', 'subspecies__name']
	list_display_add_buttons = 'name'

modeladmin_register(SpeciesAdmin)
