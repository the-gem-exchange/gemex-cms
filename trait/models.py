import importlib
# Use importlib to import from 'gemex-cms' because it's a hyphenated name
choices = importlib.import_module('.choices', 'gemex-cms')

from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import InlinePanel, FieldPanel, StreamFieldPanel, MultiFieldPanel, HelpPanel
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.search import index
from wagtail.snippets.models import register_snippet

# ===== Snippet Models =====

@register_snippet
class TraitType(index.Indexed, ClusterableModel):

	name        = models.CharField(max_length=255)
	plural_name = models.CharField(max_length=255, blank=True, null=True)

	panels = [
		FieldPanel('name', classname='full title'),
		FieldPanel('plural_name', classname='full'),
	]

	search_fields = [
		index.SearchField('name', partial_match=True),
		index.SearchField('plural_name', partial_match=True),
	]

	def plural(self):
		if self.plural_name:
			return self.plural_name
		else:
			return self.name + "s"

	def count(self):
		return Trait.objects.filter(type=self).count()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["name"]

@register_snippet
class Trait(index.Indexed, ClusterableModel):

	name    = models.CharField(max_length=255)
	image   = models.ForeignKey('image.CustomImage',     null=True, blank=True,  on_delete=models.SET_NULL)
	type    = models.ForeignKey('trait.TraitType',       null=True, blank=True,  on_delete=models.SET_NULL)
	species = models.ForeignKey('species.SubSpecies',    null=True, blank=True,  on_delete=models.SET_NULL)
	rarity  = models.CharField(choices=choices.RARITIES, null=True, blank=False, default='common', max_length=16)
	sex     = models.CharField(choices=choices.SEXES,    null=True, blank=False, default='x',    max_length=1)

	panels = [
		FieldPanel('name', classname='full title'),
		ImageChooserPanel('image'),
		MultiFieldPanel([
			FieldPanel('type', classname="no-label"),
			HelpPanel(content='<a target="_blank" href="/admin/snippets/trait/traittype/add/"><i class="icon icon-fa-plus"></i> Add a trait type</a>', classname="add-button")
		], heading='Trait Type', classname="trait-type"),
		FieldPanel('species'),
		FieldPanel('rarity'),
		FieldPanel('sex'),
	]

	search_fields = [
		index.SearchField('name', partial_match=True),
		index.SearchField('get_sex_display', partial_match=True),
		index.SearchField('rarity', partial_match=True),
		index.RelatedFields('type', [
			index.SearchField('name', partial_match=True),
			index.SearchField('plural_name', partial_match=True),
		]),
		index.RelatedFields('species', [
			index.SearchField('name', partial_match=True),
		]),
	]

	def emblem(self):
		return self.species.species.emblem if self.species.species.emblem else None

	def thumbnail(self):
		return format_html(
			'<img class="trait-thumbnail {}" src="{}" />',
			self.rarity,
			self.image.file.url if self.image else None,
		)

	def rarity_icon(self, show_text=False):
		if self.rarity == 'legendary':
			icon = 'fa-star'
		elif self.rarity == 'rare':
			icon = 'fa-square'
		elif self.rarity == 'uncommon':
			icon = 'fa-play'
		else:
			icon = 'fa-circle'

		if show_text:
			text = self.rarity.capitalize()
			return format_html(
				'<i class="icon icon-{} fa {} {}"></i> {}',
				icon, icon, self.rarity, self.rarity.capitalize()
			)
		else:
			return format_html(
				'<i class="icon icon-{} fa {} {}"></i>',
				icon, icon, self.rarity,
			)

	rarity_icon.admin_order_field = 'rarity'

	# Admin column
	def rarity_(self):
		return self.rarity_icon(show_text=True)

	# For determining sort order
	def rarity_weighted(self):
		if self.rarity == 'common':
			return 1
		if self.rarity == 'uncommon':
			return 2
		if self.rarity == 'rare':
			return 3
		if self.rarity == 'legendary':
			return 4

	def sex_icon(self, show_text=False):
		if self.sex == 'm':
			icon = 'fa-mars'
			text = 'Masculine'
		elif self.sex == 'f':
			icon = 'fa-venus'
			text = 'Feminine'
		else:
			icon = 'fa-transgender'
			text = 'Unisex'

		if show_text:
			return format_html('<i class="icon icon-{} fa {}"></i>&nbsp;&nbsp;{}',
				icon, icon, text
			)
		else:
			return format_html('<i class="icon icon-{} fa {}"></i>',
				icon, icon
			)

	# Admin column
	def sex_(self):
		return self.sex_icon(show_text=True)
	sex_.admin_order_field = 'sex'

	def sex_str_(self):
		if self.sex == 'x':
			return 'Unisex'
		if self.sex == 'f':
			return 'Female'
		if self.sex == 'm':
			return 'Male'

	def __str__(self):
		return '{} | {} | {} | {} | {}'.format(self.name, self.type, self.species, self.sex_str_(), self.rarity)

	class Meta:
		ordering = ["name"]

# ===== ModelAdmin Models =====

class TraitTypeAdmin(ModelAdmin):
	model         = TraitType
	list_display  = ('name', 'plural', 'count')
	search_fields = ['name', 'plural']

class TraitAdmin(ModelAdmin):
	model         = Trait
	list_display  = ('thumbnail', 'name', 'type', 'species', 'rarity_', 'sex_')
	search_fields = ['name', 'type__name', 'species__name', 'species__species__name', 'rarity', 'sex']
	list_display_add_buttons = 'name'
	menu_icon  = 'view'

modeladmin_register(TraitAdmin)
modeladmin_register(TraitTypeAdmin)
