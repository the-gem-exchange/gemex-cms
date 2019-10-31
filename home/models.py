from page.models import ContentPage

class HomePage(ContentPage):

	# Only available at root level
	parent_page_types = ['wagtailcore.Page']

	content_panels = ContentPage.content_panels + []

	# There can only be one HomePage
	@classmethod
	def can_create_at(cls, parent):
		return super(HomePage, cls).can_create_at(parent) and not cls.objects.exists()
