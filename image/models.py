# models.py
from django.db import models
from django.db.models.signals import pre_delete
from django.utils.functional import cached_property
from django.dispatch import receiver
from django.utils.six import string_types

from wagtail.images.image_operations import (
	DoNothingOperation, MinMaxOperation, WidthHeightOperation
)
from wagtail.images.models import (
	AbstractImage, AbstractRendition, Filter, Image
)

class CustomImage(AbstractImage):
	# Add any extra fields to image here

	# eg. To add a caption field:
	# caption = models.CharField(max_length=255, blank=True)

	admin_form_fields = Image.admin_form_fields + (
		# Then add the field names here to make them appear in the form:
		# 'caption',
	)

	def get_rendition(self, rendition_filter):
		"""Always return the source image file for GIF renditions.

		CustomImage overrides the default Wagtail renditions behavior to
		always embed the original uploaded image file for GIFs, instead of
		generating new versions on the fly.
		"""
		if self.file.name.endswith('.gif'):
			return self.get_mock_rendition(rendition_filter)
		else:
			return super(CustomImage, self).get_rendition(rendition_filter)

	def get_mock_rendition(self, rendition_filter):
		"""Create a mock rendition object that wraps the original image.

		Using the template tag {% image image 'original' %} will return an
		<img> tag linking to the original file (instead of a file copy, as
		is default Wagtail behavior).

		Template tags with Wagtail size-related filters (width, height, max,
		and min), e.g. {% image image 'max-165x165' %}, will generate an
		<img> tag with appropriate size parameters, following logic from
		wagtail.images.image_operations.
		"""
		if isinstance(rendition_filter, string_types):
			rendition_filter = Filter(spec=rendition_filter)

		width = self.width
		height = self.height

		for operation in rendition_filter.operations:
			if isinstance(operation, DoNothingOperation):
				continue

			if not any([
				isinstance(operation, WidthHeightOperation),
				isinstance(operation, MinMaxOperation),
			]):
				raise RuntimeError('non-size operations not supported on GIFs')

			width, height = self.apply_size_operation(operation, width, height)

		return CustomRendition(
			image=self,
			file=self.file,
			width=width,
			height=height
		)

	@staticmethod
	def apply_size_operation(operation, width, height):
		class MockResizableImage(object):
			def __init__(self, width, height):
				self.width = width
				self.height = height

			def get_size(self):
				return self.width, self.height

			def resize(self, size):
				width, height = size
				self.width = width
				self.height = height

		mock_image = MockResizableImage(width, height)
		operation.run(mock_image, image=None, env={})
		return mock_image.width, mock_image.height

	# If the image is both large and its height-to-width ratio is approximately
	# 1/2 we instruct the template to render large Twitter cards
	# See https://dev.twitter.com/cards/types/summary-large-image
	@property
	def should_display_summary_large_image(self):
		image_ratio = float(self.height) / self.width
		return self.width >= 1000 and 0.4 <= image_ratio <= 0.6

	@cached_property
	def orientation(self):
		if self.is_portrait:
			return 'portrait'
		elif self.is_landscape:
			return 'landscape'
		elif self.is_square:
			return 'square'
		else:
			return None

	@cached_property
	def is_square(self):
		return self.height == self.width

	@cached_property
	def is_portrait(self):
		return self.height > self.width

	@cached_property
	def is_landscape(self):
		return self.height < self.width


class CustomRendition(AbstractRendition):
	image = models.ForeignKey(CustomImage, on_delete=models.CASCADE, related_name='renditions')

	class Meta:
		unique_together = (
			('image', 'filter_spec', 'focal_point_key'),
		)


# Delete the source image file when an image is deleted
@receiver(pre_delete, sender=CustomImage)
def image_delete(sender, instance, **kwargs):
	instance.file.delete(False)


# Delete the rendition image file when a rendition is deleted
@receiver(pre_delete, sender=CustomRendition)
def rendition_delete(sender, instance, **kwargs):
	instance.file.delete(False)
