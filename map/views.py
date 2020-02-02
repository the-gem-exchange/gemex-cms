from django.shortcuts import render

from map.models import MapLocation

def map_page(request):
	return render(request, 'map/map.html', {
		'nodes': MapLocation.objects.all()
	})
