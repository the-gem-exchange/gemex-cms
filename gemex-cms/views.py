from django.shortcuts import render

from trait.models import Trait, TraitType
from species.models import Species, SubSpecies

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
