from page.models import ContentPage

class HomePage(ContentPage):

	# Only available at root level
	parent_page_types = ['wagtailcore.Page']

	content_panels = ContentPage.content_panels + []

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

		return context
