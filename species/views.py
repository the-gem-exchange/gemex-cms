from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render

from species.models import Species, SubSpecies


def species(request):
	species = Species.objects.all()
	return render(request, 'species.html', {
		'species': species,
	})
