from trait.site_summary import TraitSummaryItem

from wagtail.core import hooks

@hooks.register('construct_homepage_summary_items')
def add_trait_summary_item(request, items):
	items.append(TraitSummaryItem(request))
