from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from wagtail.api import APIField
from wagtail.api.v2.endpoints import BaseAPIEndpoint

class ComicPage(Page):
    page_number = models.IntegerField()
    comic = models.ForeignKey(
        'image.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + []

    content_panels = Page.content_panels + [
        FieldPanel('page_number'),
        ImageChooserPanel('comic'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]

    api_fields = [
        APIField('title'),
        APIField('comic'),
        APIField('page_number'),
    ]
