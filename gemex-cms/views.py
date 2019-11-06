from django.http import HttpResponseRedirect
from django.shortcuts import render

from trait.models import Trait, TraitType
from species.models import Species, SubSpecies
from comic.models import ComicPage

def traits(request, id=None):
	if id:
		species = SubSpecies.objects.get(id=id)
		traits = species.traits()
	else:
		species = None
		traits = Trait.objects.all()

	return render(request, 'traits.html', {
		'species': species,
		'traits':  traits,
	})

def species(request):
	species = Species.objects.all()
	return render(request, 'species.html', {
		'species': species,
	})

def comic(request, page=1):
	page_number = int(page)
	page_count  = ComicPage.objects.live().all().count()

	if not page or page_number > page_count:
		return HttpResponseRedirect('/comic/{}/'.format(page_count))
	elif page_number < 1:
		return HttpResponseRedirect('/comic/1/')
	else:
		comic_page = ComicPage.objects.live().get(page_number=page)

	return render(request, 'comic/page.html', {
		'comic':        comic_page,
		'page_count':   page_count,
		'next_page':    page_number + 1 if page_number < page_count else None,
		'prev_page':    page_number - 1 if page_number > 1 else None,
		'current_page': page_number
	})
