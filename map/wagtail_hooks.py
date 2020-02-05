from .site_summary import MapSummaryItem

from wagtail.core import hooks

@hooks.register('construct_homepage_summary_items')
def add_map_summary_item(request, items):
	items.append(MapSummaryItem(request))
