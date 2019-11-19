from .models import ComicFolder, ComicPage

from django.http import HttpResponseRedirect

def comic_page(request, page_number=None):
	if page_number:
		page = ComicPage.objects.live().get(page_number=int(page_number))
		if page:
			return HttpResponseRedirect(page.url)

	return HttpResponseRedirect(ComicFolder.objects.first().url)
