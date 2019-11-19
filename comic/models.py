from django.db import models
from django.http import HttpResponseRedirect

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

	banner_image = models.ForeignKey('image.CustomImage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

	content_panels = AbstractFolder.content_panels + [
		ImageChooserPanel('banner_image')
	]

	def serve(self, request, *args, **kwargs):
		first_child = self.get_children().live().first()
		return HttpResponseRedirect(first_child.url)


class ComicChapter(AbstractFolder):
	subpage_types     = ['ComicPage']
	parent_page_types = ['ComicFolder']

	chapter_number = models.IntegerField()

	content_panels = AbstractFolder.content_panels + [
		FieldPanel('chapter_number', classname="title full"),
	]

	def serve(self, request, *args, **kwargs):
		first_child = self.get_children().live().last() # Get latest page
		return HttpResponseRedirect(first_child.url)


class ComicPage(AbstractPage):

	parent_page_types = ['ComicChapter']

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

	def get_context(self, request):
		context = super(ComicPage, self).get_context(request)
		page_count = ComicPage.objects.live().all().count()

		context['banner_image'] = ComicFolder.objects.first().banner_image
		context['page_count']   = page_count
		context['next_page']    = self.page_number + 1 if self.page_number < page_count else None
		context['prev_page']    = self.page_number - 1 if self.page_number > 1 else None

		return context

	def save(self, *args, **kwargs):
		self.slug = 'page-{}'.format(self.page_number)
		super(ComicPage, self).save(*args, **kwargs)

	class Meta:
		ordering = ["page_number"]
