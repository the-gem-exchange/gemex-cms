from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query


def home(request):
    page = request.GET.get('page', 1)

    return render(request, 'home/home.html', {
        'page': page
    })
