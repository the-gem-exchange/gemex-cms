from django.utils.html import format_html, format_html_join
from django.contrib.staticfiles.templatetags.staticfiles import static

from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from wagtail.core import hooks

@hooks.register('insert_global_admin_css')
def global_admin_css():
	return format_html('<link rel="stylesheet" href={}>',static('css/admin.css'))

# Hide "Snippets" menu - we'll be using ModelAdmin menus instead
# "Images" and "Documents" will be under the "Files" folder
@hooks.register('construct_main_menu')
def hide_menu_items(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name not in ['snippets','images','documents']]

@hooks.register('register_admin_menu_item')
def register_files_submenu():
	return SubmenuMenuItem(
		'Files',
		Menu(
			register_hook_name='register_files_menu_item',
			construct_hook_name='construct_files_menu'
		),
		classnames='icon icon-image',
		order=200
	)

@hooks.register('register_files_menu_item')
def register_dashboard_menu_item():
	return MenuItem('Documents', '/admin/documents/', classnames='icon icon-doc-full-inverse')

@hooks.register('register_files_menu_item')
def register_dashboard_menu_item():
	return MenuItem('Images', '/admin/images/', classnames='icon icon-image')
