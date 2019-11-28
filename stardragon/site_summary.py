from stardragon.models import Stardragon

from wagtail.admin.site_summary import SummaryItem

class StardragonSummaryItem(SummaryItem):
	template = 'wagtailadmin/home/site_summary_stardragons.html'

	def get_context(self):
		count = Stardragon.objects.count()
		return { 'count': count }
