from django.db import models

from modelcluster.fields import ParentalKey

from page.models import AbstractPage, AbstractFolder

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from wagtail.api import APIField
from wagtail.api.v2.endpoints import BaseAPIEndpoint


# Parent folder for all comics
class ComicFolder(AbstractFolder):
	subpage_types     = ['ComicChapter']
	parent_page_types = ['home.HomePage']


class ComicChapter(AbstractFolder):
	subpage_types     = ['ComicPage']
	parent_page_types = ['ComicFolder']

	chapter_number = models.IntegerField()

	content_panels = ComicFolder.content_panels + [
		FieldPanel('chapter_number', classname="title full"),
	]


class ComicPage(AbstractPage):

	page_number = models.IntegerField()

	comic = models.ForeignKey(
		'image.CustomImage',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)

	content_panels = AbstractPage.content_panels + [
		FieldPanel('page_number', classname="title full"),
		ImageChooserPanel('comic'),
	]

	search_fields = AbstractPage.search_fields + []

	api_fields = [
		APIField('title'),
		APIField('comic'),
		APIField('page_number'),
	]

	def chapter(self):
		return self.get_parent()

	class Meta:
		ordering = ["page_number"]
