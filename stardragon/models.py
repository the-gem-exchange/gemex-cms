import importlib
# Use importlib to import from 'gemex-cms' because it's a hyphenated name
choices = importlib.import_module('.choices', 'gemex-cms')

import datetime

from django.db import models
from django.utils import timezone
from django.utils.html import format_html

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import InlinePanel, FieldPanel, HelpPanel, MultiFieldPanel
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

DESIGN_TYPES = [
	('official', 'Official'),
	('slot',     'MYO Slot'),
	('myo',      'Make Your Own'),
]

# ===== Stardragon Snippet =====

@register_snippet
class Stardragon(index.Indexed, ClusterableModel):

	# ========== Fields ==========

	design_type = models.CharField(choices=DESIGN_TYPES, null=True, blank=False, default='official', max_length=255)

	name        = models.CharField(max_length=255)
	base        = models.CharField(max_length=255, blank=True)
	buyer_email = models.CharField(max_length=255, blank=True)

	price = models.IntegerField(default=0)

	# Mutliple Choice
	rarity = models.CharField(choices=choices.RARITIES, null=True, blank=False, default='common', max_length=16)
	sex    = models.CharField(choices=choices.SEXES,    null=True, blank=False, default='x',      max_length=1)

	# ID's
	serial_number = models.CharField(max_length=255, blank=True) # Used to redeem slots
	invoice_id    = models.CharField(max_length=255, blank=True) # Used to track Paypal invoices

	# Boolean Flags
	paid     = models.BooleanField(default=False, verbose_name="Paid?")
	approved = models.BooleanField(default=False, verbose_name="Approved?")

	# Dates
	post_date     = models.DateTimeField(blank=True, null=True) # Date it goes live
	purchase_date = models.DateTimeField(blank=True, null=True) # Date the MYO was purchased

	notes = models.TextField(blank=True)

	# ========== Panels ==========

	panels = [
		FieldPanel('name', classname="full title collapsible"),

		FieldPanel('design_type', classname="collapsible"),

		MultiFieldPanel([
			# HelpPanel(content=""),
			FieldPanel('base'),
			FieldPanel('rarity'),
			FieldPanel('sex'),
			HelpPanel(content="<hr style='margin:0;' />"),
			InlinePanel('species', label='Species'),
			HelpPanel(content="<hr style='margin:0;' />"),
			InlinePanel('traits',  label='Traits'),
			HelpPanel(content="<hr style='margin:0;' />"),
			InlinePanel('images',  label='Images'),
			HelpPanel(content="<hr style='margin:0;' />"),
			InlinePanel('colors',  label='Colors'),
			HelpPanel(content="<hr style='margin:0;' />"),
			InlinePanel('links',   label='Links'),
		], heading="Stardragon Info",
		classname="collapsible"),

		MultiFieldPanel([
			# HelpPanel(content=""),
			FieldPanel('invoice_id'),
			FieldPanel('purchase_date'),
			FieldPanel('price'),
			FieldPanel('paid'),
		], heading="Purchase Info",
		classname="collapsible collapsed"),

		MultiFieldPanel([
			# HelpPanel(content=""),
			FieldPanel('serial_number'),
			FieldPanel('buyer_email'),
		], heading="Make Your Own Info",
		classname="collapsible collapsed"),

		MultiFieldPanel([
			# HelpPanel(content=""),
			FieldPanel('notes'),
			InlinePanel('designers', label="Designer"),
			FieldPanel('post_date'),
			FieldPanel('approved'),
		], heading="Publishing Info",
		classname="collapsible"),
	]

	# ========== Methods ==========

	# TODO: Apply watermark
	def thumbnail(self):
		image = self.images.first()
		if image:
			return format_html(
				'<img class="species-thumbnail" src="{}" />',
				image.image.file.url,
			)
		else:
			return None

	def species_(self):
		count = self.species.count()
		if  count == 1:
			return self.species.first().species.name
		elif count > 1:
			return "Hybrid"
		else:
			return None

	# Determine if a Stardragon shows to anonymous users
	# Must be marked as paid and aprroved
	# If a post date is set, it should be in the past
	def is_public(self):
		if self.post_date:
			posted = self.post_date < timezone.now()
		else:
			posted = True
		return self.paid and self.approved and posted

	# If it has more than one species, it's a hybrid
	def is_hybrid(self):
		return len(self.species.all()) > 1

	def __str__(self):
		return self.name


# ================ Orderable Classes ===============
# Fields that have one or more entry, have multiple sub-fields, or both

class StardragonLink(Orderable):
	stardragon = ParentalKey('Stardragon', related_name='links', on_delete=models.CASCADE)

	LINK_TYPES = [
		('sale_posting', 'Sale Posting'),
		('furaffinity',  'Furaffinity'),
		('deviantart',   'Deviantart'),
		('other',        'Other')
	]

	name = models.CharField(max_length=255, blank=True)
	url  = models.CharField(max_length=255, blank=True)
	type = models.CharField(max_length=255, choices=LINK_TYPES, blank=True)

	panels = [
		FieldPanel('name'),
		FieldPanel('url'),
		FieldPanel('type')
	]


class StardragonImage(Orderable):
	stardragon = ParentalKey('Stardragon', related_name='images', on_delete=models.CASCADE)

	image = models.ForeignKey(
		'image.CustomImage',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)

	panels = [ImageChooserPanel('image')]


class StardragonSpecies(Orderable):
	stardragon = ParentalKey('Stardragon', related_name='species', on_delete=models.CASCADE)

	species = models.ForeignKey('species.Species', null=True, blank=True, on_delete=models.SET_NULL)

	panels = [FieldPanel('species')]


class StardragonTrait(Orderable):
	stardragon = ParentalKey('Stardragon', related_name='traits', on_delete=models.CASCADE)

	trait = models.ForeignKey('trait.Trait', null=True, blank=True, on_delete=models.SET_NULL)

	panels = [SnippetChooserPanel('trait', 'trait.Trait')]


class StardragonColorPalette(Orderable):
	stardragon = ParentalKey('Stardragon', related_name='colors', on_delete=models.CASCADE)

	color = models.CharField(max_length=255, blank=True)

	panels = [FieldPanel('color', classname='use-colorpicker')]


class StardragonDesigner(Orderable):
	stardragon = ParentalKey('Stardragon', related_name='designers', on_delete=models.CASCADE)

	designer = models.CharField(max_length=255, blank=True)

	panels = [FieldPanel('designer')]

# ===== ModelAdmin Classes =====

class StardragonAdmin(ModelAdmin):
	model         = Stardragon
	menu_icon     = 'user'
	list_display  = ('thumbnail', 'name','design_type', 'species_', 'is_public')
	search_fields = ['name', 'design_type']
	list_display_add_buttons = 'name'

modeladmin_register(StardragonAdmin)
