from stardragon.site_summary import StardragonSummaryItem

from wagtail.core import hooks

@hooks.register('construct_homepage_summary_items')
def add_stardragon_summary_item(request, items):
	items.append(StardragonSummaryItem(request))
