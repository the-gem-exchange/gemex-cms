from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render

from trait.models import Trait, TraitType
from species.models import Species, SubSpecies
from comic.models import ComicPage, ComicFolder

def traits(request, id=None):
	if id:
		species = SubSpecies.objects.get(id=id)
		traits  = species.traits()
	else:
		species = None
		traits  = Trait.objects.all()

	species_list = Species.objects.all()

	traits_by_type = []
	trait_types    = Trait.objects.order_by().values('type').distinct()
	for t in trait_types:
		obj = {
			'type':   TraitType.objects.get(id=t.get('type')),
			'traits': traits.filter(type__id=t.get('type'))
		}
		if(obj['traits'].count() > 0):
			traits_by_type.append(obj)


	return render(request, 'trait/index.html', {
		'traits_by_type': traits_by_type,
		'species':        species,
		'species_list':   species_list,
		'traits':         traits,
	})

def species(request):
	species = Species.objects.all()
	return render(request, 'species.html', {
		'species': species,
	})
