from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.models import ClusterableModel

from species.models import Species

from wagtail.admin.edit_handlers import InlinePanel, FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.search import index
from wagtail.snippets.models import register_snippet

@register_snippet
class Trait(index.Indexed, ClusterableModel):

	name  = models.CharField(max_length=255)
	image = models.ForeignKey('image.CustomImage', null=True, blank=True, on_delete=models.SET_NULL)

	type = models.CharField(
		max_length=24,
		blank=False,
		null=True,
		choices=[
			('accessory',  'Accessory'),
			('arm',        'Arm'),
			('barbel',     'Barbel'),
			('body',       'Body'),
			('crest',      'Crest'),
			('cape',       'Cape'),
			('collar',     'Collar'),
			('ear',        'Ear'),
			('fluff',      'Fluff'),
			('face',       'Face'),
			('foot',       'Foot'),
			('fur',        'Fur'),
			('fin',        'Fin'),
			('gem',        'Gem'),
			('head',       'Head'),
			('hip-skirt',  'Hip Skirt'),
			('horn',       'Horn'),
			('hand',       'Hand'),
			('hip',        'Hip'),
			('leg',        'Leg'),
			('other',      'Other'),
			('poncho',     'Poncho'),
			('shale',      'Shale'),
			('tail-shard', 'Tail Shard'),
			('tail',       'Tail'),
			('tail-plate', 'Tail Plate'),
			('tail-prong', 'Tail Prong'),
			('whisker',    'Whisker'),
			('wing',       'Wing'),
		]
	)

	species = models.ForeignKey('species.Species', null=True, blank=True, on_delete=models.SET_NULL)

	subspecies = models.CharField(
		max_length=24,
		blank=True,
		default='none',
		choices=[
			('none',        'None'),
			('arctic',      'Arctic'),
			('desert',      'Desert'),
			('deepforge',   'Deepforge'),
			('deepsea',     'Deepsea'),
			('drenched',    'Drenched'),
			('fuu',         'Fuu'),
			('kelpie',      'Kelpie'),
			('mountain',    'Mountain'),
			('mudskipper',  'Mudskipper'),
			('sheep',       'Sheep'),
			('saber',       'Saber'),
			('sloth',       'Sloth'),
			('severblight', 'Severblight'),
			('tropical',    'Tropical'),
			('vampire',     'Vampire'),
		]
	)

	rarity = models.CharField(
		max_length=24,
		blank=False,
		null=True,
		default='none',
		choices=[
			('none',      'None'),
			('common',    'Common'),
			('uncommon',  'Uncommon'),
			('rare',      'Rare'),
			('legendary', 'Legendary'),
		]
	)

	sex = models.CharField(
		max_length=24,
		blank=False,
		default='x',
		null=True,
		choices=[
			('x', 'Any'),
			('f', 'Female'),
			('m', 'Male'),
		]
	)

	panels = [
		FieldPanel('name'),
		FieldPanel('type'),
		ImageChooserPanel('image'),
		MultiFieldPanel([
			FieldPanel('species'),
			FieldPanel('subspecies'),
		], heading="Species"),
		FieldPanel('rarity'),
		FieldPanel('sex'),
	]

	def __str__(self):
		return self.name
