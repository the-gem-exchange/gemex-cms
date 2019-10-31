from page.stream_blocks import stream_blocks

from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel


# === Abstract Page Models ===

class AbstractFolder(Page):

	content_panels = Page.content_panels
	
	class Meta:
		abstract = True


class AbstractPage(Page):

	content_panels = Page.content_panels

	class Meta:
		abstract = True


# All pages that use StreamField content should inherit from this model
class ContentPage(AbstractPage):

	content = StreamField(stream_blocks, blank=True)

	content_panels = AbstractPage.content_panels + [
		StreamFieldPanel('content'),
	]

	class Meta:
		abstract = True

# === Basic Page Models ===

class Folder(AbstractFolder):
	pass

class BasicPage(ContentPage):
	pass
