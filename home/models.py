from django.db import models

from page.models import ContentPage

from species.models import SubSpecies

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import InlinePanel
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(ContentPage):

	# Only available at root level
	parent_page_types = ['wagtailcore.Page']

	content_panels = [
		InlinePanel('hero_image_layers', label="Hero Image Layers", help_text="Bottom-most layer goes first.")
	] + ContentPage.content_panels

	# There can only be one HomePage
	@classmethod
	def can_create_at(cls, parent):
		return super(HomePage, cls).can_create_at(parent) and not cls.objects.exists()

	def get_context(self, request):
		context = super(HomePage, self).get_context(request)

		context['links'] = [
			{
				"name":"Patreon",
				"icon":"fab fa-patreon",
				"link":"https://www.patreon.com/GemExchange"
			},
			{
				"name":"Toyhouse",
				"icon":"fa fa-home",
				"link":"http://toyhou.se/~world/1420.gemexchange-jo-arca"
			},
			{
				"name":"FurAffinity",
				"icon":"fa fa-paw",
				"link":"https://www.furaffinity.net/user/gemexchange"
			},
			{
				"name": "Twitter",
				"icon":"fab fa-twitter",
				"link":"https://twitter.com/Gem_Exchange"
			},
			{
				"name":"Github",
				"icon":"fab fa-github",
				"link":"https://github.com/juan0tron/the-gem-exchange"
			},
			{
				"name":"DeviantArt",
				"icon":"fab fa-deviantart",
				"link":"https://gemexchange.deviantart.com/"
			},
			{
				"name":"Discord",
				"icon":"fab fa-discord",
				"link":"https://discord.gg/T9Xrjs5"
			}
		]

		context['compendium_backgrounds'] = SubSpecies.objects.filter(name="Standard").exclude(background__isnull=True)[:3]

		return context


class HeroLayer(Orderable):
	home_page = ParentalKey('HomePage', related_name='hero_image_layers', on_delete=models.CASCADE)

	image = models.ForeignKey('image.CustomImage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

	panels = [ ImageChooserPanel('image') ]
