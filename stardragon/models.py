import importlib
# Use importlib to import from 'gemex-cms' because it's a hyphenated name
choices = importlib.import_module('.choices', 'gemex-cms')

from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import InlinePanel, FieldPanel, HelpPanel, MultiFieldPanel
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

DESIGN_TYPES = [
	('official', 'Official'),
	('slot',     'Slot'),
	('myo',      'Make Your Own'),
]

# ===== Stardragon Snippet =====

@register_snippet
class Stardragon(index.Indexed, ClusterableModel):

	# ========== Fields ==========

	design_type = models.CharField(choices=DESIGN_TYPES, null=True, blank=False, default='official', max_length=255)

	name        = models.CharField(max_length=255)
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

	# ========== Panels ==========

	panels = [
		FieldPanel('name', classname="full title collapsible"),

		FieldPanel('design_type', classname="collapsible"),

		MultiFieldPanel([
			# HelpPanel(content=""),
			FieldPanel('rarity'),
			FieldPanel('sex'),
			InlinePanel('species', label='Species'),
			InlinePanel('traits', label='Traits'),
			InlinePanel('images', label='Images'),
			InlinePanel('colors', label='Colors'),
			InlinePanel('links', label='Links'),
		], heading="Stardragon Info", classname="collapsible"),

		MultiFieldPanel([
			# HelpPanel(content=""),
			FieldPanel('invoice_id'),
			FieldPanel('purchase_date'),
			FieldPanel('price'),
			FieldPanel('paid'),
		], heading="Purchase Info", classname="collapsible collapsed"),

		MultiFieldPanel([
			# HelpPanel(content=""),
			FieldPanel('serial_number'),
			FieldPanel('buyer_email'),
		], heading="Make Your Own Info", classname="collapsible collapsed"),

		MultiFieldPanel([
			# HelpPanel(content=""),
			InlinePanel('designers', label="Designer"),
			FieldPanel('post_date'),
			FieldPanel('approved'),
		], heading="Publishing Info", classname="collapsible"),
	]

	# ========== Methods ==========

	def thumbnail(self):
		# grab image[0] and apply watermark
		# return format_html(<img src="rendition with watermark">)
		pass

	def is_public(self):
		#if paid == true and approved == true and sale_date in the past
		pass

	# If it has more than one species, it's a hybrid
	# If all subspecies have the same parent species, it's not a hybrid
	def is_hybrid(self):
		# return len(self.species.all().distinct(species)) > 1
		pass

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

	subspecies = models.ForeignKey('species.SubSpecies', null=True, blank=True, on_delete=models.SET_NULL)

	panels = [FieldPanel('subspecies')]


class StardragonTrait(Orderable):
	stardragon = ParentalKey('Stardragon', related_name='traits', on_delete=models.CASCADE)

	trait = models.ForeignKey('trait.Trait', null=True, blank=True, on_delete=models.SET_NULL)

	panels = [FieldPanel('trait')]


class StardragonColorPalette(Orderable):
	stardragon = ParentalKey('Stardragon', related_name='colors', on_delete=models.CASCADE)

	color = models.CharField(max_length=255, blank=True)

	panels = [FieldPanel('color')]


class StardragonDesigner(Orderable):
	stardragon = ParentalKey('Stardragon', related_name='designers', on_delete=models.CASCADE)

	designer = models.CharField(max_length=255, blank=True)

	panels = [FieldPanel('designer')]

# ===== ModelAdmin Classes =====

class StardragonAdmin(ModelAdmin):
	model         = Stardragon
	menu_icon     = 'user'
	list_display  = ('name','design_type')
	search_fields = ['name', 'design_type']

modeladmin_register(StardragonAdmin)
