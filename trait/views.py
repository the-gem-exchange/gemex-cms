from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render

from species.models import Species, SubSpecies

from trait.models import Trait, TraitType


def trait_page(request):
	species_name    = request.GET.get('species', None)
	subspecies_name = request.GET.get('subspecies', None)
	trait_types     = TraitType.objects.all()
	species         = None
	parent_species  = None
	title           = "Traits Compendium"

	if species_name and subspecies_name:
		species  = SubSpecies.objects.get(name__icontains=subspecies_name, species__name__icontains=species_name)
		subtypes = species.species.subspecies.all()
		traits   = species.traits()
		title    += ' - ' + species.name + ' ' + species.species.name + 's'
		parent_species = species.species
	elif species_name:
		species  = Species.objects.get(name__icontains=species_name)
		subtypes = species.subspecies.all()
		traits   = species.traits()
		title    += ' - ' + species.name + 's'
		parent_species = species
	else:
		subtypes = SubSpecies.objects.all()
		traits   = Trait.objects.all()

	traits_by_type = []
	for type in trait_types:
		obj = {
			'type':   TraitType.objects.get(id=type.id),
			'traits': sorted(traits.filter(type__id=type.id), key=lambda trait: trait.rarity_weighted())
		}
		if(len(obj['traits']) > 0):
			traits_by_type.append(obj)

	data = {
		'trait_types':    trait_types,
		'traits_by_type': traits_by_type,
		'species':        species,
		'species_name':   species_name,
		'subtypes':       subtypes,
		'species_list':   Species.objects.all(),
		'traits':         traits,
		'title':          title,
		'parent_species': parent_species
	}

	return render(request, 'trait/index.html', data)
