from trait.models import Trait

from wagtail.admin.site_summary import SummaryItem

class TraitSummaryItem(SummaryItem):
	template = 'wagtailadmin/home/site_summary_traits.html'

	def get_context(self):
		count = Trait.objects.count()
		return { 'count': count }
