from .models import ComicFolder, ComicPage

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render


def comic_page(request, page_number=None):
	if page_number:
		page = ComicPage.objects.live().get(page_number=int(page_number))
		if page:
			return HttpResponseRedirect(page.url)

	return HttpResponseRedirect(ComicFolder.objects.first().url)


def comic_archive(request, page_number=None):

	pages = ComicPage.objects.live()

	# Pagination
	items_per_page = 20
	paginator = Paginator(pages, items_per_page)
	try:
		paginated_results = paginator.page(page_number)
	except PageNotAnInteger:
		paginated_results = paginator.page(1)
	except EmptyPage:
		paginated_results = paginator.page(paginator.num_pages)

	return render(request, 'comic/archive.html', {
		'pages':   paginated_results,
		'archive': True,
		'banner_image': ComicFolder.objects.first().banner_image,
	})
