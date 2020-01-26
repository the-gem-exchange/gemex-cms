from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from .api import api_router

from comic.views import comic_page

from search import views as search_views

from trait.views import trait_page

from bot.views import get_command

urlpatterns = [
	url(r'^django-admin/', admin.site.urls),

	url(r'^admin/', include(wagtailadmin_urls)),
	url(r'^documents/', include(wagtaildocs_urls)),

	url(r'^search/$', search_views.search, name='search'),

	# API Endpoints
	url(r'^api/', api_router.urls),

	url(r'^bot-commands/(?P<command>\w+)/$', get_command),

	url(r'^comic/(?P<page_number>\d+)/$', comic_page),

	url(r'^traits/$', trait_page),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
