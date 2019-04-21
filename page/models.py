from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

import page.stream_blocks as StreamBlocks

availableStreamBlocks = [
    ('heading',       blocks.CharBlock(classname="full title")),
    ('paragraph',     blocks.RichTextBlock()),
    ('image',         ImageChooserBlock()),
    ('Two_Columns',   StreamBlocks.TwoColumns(icon='two-columns')),
    ('Three_Columns', StreamBlocks.ThreeColumns(icon='three-columns')),
]

class BasicPage(Page):
    content = StreamField(availableStreamBlocks, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = 'Basic Page'
