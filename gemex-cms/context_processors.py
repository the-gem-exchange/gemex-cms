import os
from django.conf import settings

def export_vars(request):
	data = {}
	data['VERSION'] = settings.VERSION
	return data
