from wagtail.core import hooks
from django.utils.html import format_html, format_html_join
from django.contrib.staticfiles.templatetags.staticfiles import static

@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href={}>',static('css/admin.css'))
