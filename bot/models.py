from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from markdown import markdown

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import InlinePanel, FieldPanel
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


@register_snippet
class BotCommand(index.Indexed, ClusterableModel):

	command = models.CharField(max_length=255)

	type = models.CharField(
		choices=[
			('text',  'Text'),
			('image', 'Image')
		],
		null=True,
		blank=False,
		default='text',
		max_length=255
	)

	text = models.TextField(blank=True, help_text="Supports markdown formatting.")

	panels = [
		FieldPanel('command'),
		FieldPanel('type'),
		FieldPanel('text'),
		InlinePanel('image', label="Image (Upload multiple for a random image)"),
	]

	# For modeladmin column view
	def _command(self):
		return "!" + self.command

	# For modeladmin column view
	def _message(self):
		if not self.image and not self.text:
			return None
		if self.type == 'text':
			text = self.text.replace('\\n','<br>') # Markdown lib doesn't convert newlines to <br>'s for some reason
			return format_html(
				'<div class="discord-message">' + markdown(text) + '</div>'
			)
		if self.type == 'image':
			image = self.get_image()
			return format_html(
				'<img class="species-thumbnail" src="{}" />',
				image.image.file.url if image else None,
			)

	def __str__(self):
		return self.command

	def get_image(self):
		if self.image.count() == 1:
			return self.image.first()
		elif self.image.count() > 1:
			# pick a random image
			return self.image.order_by('?').first()

	class Meta:
		ordering = ["command"]


class BotCommandImage(Orderable):

	command = ParentalKey(BotCommand, on_delete=models.CASCADE, related_name='image')

	image = models.ForeignKey(
		'image.CustomImage',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name="bot_command_image"
	)

	panels = [
		ImageChooserPanel('image'),
	]


class BotCommandAdmin(ModelAdmin):
	model         = BotCommand
	menu_icon     = 'code'
	list_display  = ('_command', '_message')
	search_fields = ['command', 'text']
	list_display_add_buttons = '_command'

modeladmin_register(BotCommandAdmin)
