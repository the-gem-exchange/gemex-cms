from comic.site_summary import ComicPageSummaryItem, ComicChapterSummaryItem

from wagtail.core import hooks

@hooks.register('construct_homepage_summary_items')
def add_comic_page_summary_item(request, items):
	items.append(ComicPageSummaryItem(request))

# @hooks.register('construct_homepage_summary_items')
# def add_comic_chapter_summary_item(request, items):
# 	items.append(ComicChapterSummaryItem(request))
