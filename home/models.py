from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from wagtail.api import APIField
from wagtail.api.v2.endpoints import BaseAPIEndpoint

import page.stream_blocks as StreamBlocks

availableStreamBlocks = [
    ('Title',         StreamBlocks.SectionTitle(icon='title')),
    ('Subtitle',      StreamBlocks.SubTitle(icon='title')),
    ('heading',       blocks.CharBlock(classname="full title")),
    ('paragraph',     blocks.RichTextBlock()),
    ('image',         ImageChooserBlock()),
    ('One_Column',    StreamBlocks.OneColumn(icon='one-column')),
    ('Two_Columns',   StreamBlocks.TwoColumns(icon='two-columns')),
    ('Three_Columns', StreamBlocks.ThreeColumns(icon='three-columns')),
]

class HomePage(Page):
    content = StreamField(availableStreamBlocks, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    api_fields = [
        APIField('title'),
        APIField('content'),
    ]
