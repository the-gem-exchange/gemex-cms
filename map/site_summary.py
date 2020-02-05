from map.models import MapLocation

from wagtail.admin.site_summary import SummaryItem

class MapSummaryItem(SummaryItem):
	template = 'map/site_summary_comic_pages.html'

	def get_context(self):
		count = MapLocation.objects.all().count()
		return {
			'link': '/admin/map/maplocation/',
			'count': count
		}
