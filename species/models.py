from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import InlinePanel, FieldPanel
from wagtail.core.models import Orderable
from wagtail.search import index
from wagtail.snippets.models import register_snippet

@register_snippet
class Species(index.Indexed, ClusterableModel):

	name = models.CharField(max_length=255)

	panels = [
		FieldPanel('name'),
		InlinePanel('subspecies', label="Subspecies"),
	]

	def __str__(self):
		return self.name


class SubSpecies(Orderable):
	species = ParentalKey(Species, on_delete=models.CASCADE, related_name='subspecies')
	name    = models.CharField(max_length=255)

	panels = [
		FieldPanel('name'),
	]

	def __str__(self):
		return self.name
