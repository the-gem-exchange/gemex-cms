from comic.models import ComicPage, ComicChapter, ComicFolder

from wagtail.admin.site_summary import SummaryItem

class ComicChapterSummaryItem(SummaryItem):
	template = 'wagtailadmin/home/site_summary_comic_chapters.html'

	def get_context(self):
		count = ComicChapter.objects.live().all().count()
		return { 'count': count }

class ComicPageSummaryItem(SummaryItem):
	template = 'wagtailadmin/home/site_summary_comic_pages.html'

	def get_context(self):
		count = ComicPage.objects.live().all().count()
		return {
			'root_id': ComicFolder.objects.first().id,
			'count': count
		}
