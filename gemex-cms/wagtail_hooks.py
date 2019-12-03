from django.utils.html import format_html, format_html_join
from django.contrib.staticfiles.templatetags.staticfiles import static

from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from wagtail.core import hooks

# ========== CSS ==========

@hooks.register('insert_global_admin_css')
def global_admin_color_picker_css():
	return format_html('<link rel="stylesheet" href="{}">', static('/css/vendor/spectrum.css'))

@hooks.register('insert_global_admin_css')
def code_editor_css():
	return format_html(
		"""
		<link rel="stylesheet" href={}>
		<link rel="stylesheet" href={}>
		""",
		static('admin/css/codemirror-dracula-theme.css'),
		'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.9.0/codemirror.css'
	)


@hooks.register('insert_global_admin_css')
def global_admin_css():
	return format_html('<link rel="stylesheet" href={}>',static('css/admin.css'))


# ========== JS ==========

@hooks.register('insert_global_admin_js')
def global_admin_color_picker_js():
	return format_html(
		'<script type="text/javascript" src="{}"></script>',
		static('/js/vendor/spectrum.js')
	)

@hooks.register('insert_global_admin_js')
def code_editor_js():
	return format_html(
		"""
		<script type="text/javascript" src="{}"></script>
		<script type="text/javascript" src="{}"></script>
		<script type="text/javascript" src="{}"></script>
		<script type="text/javascript" src="{}"></script>
		""",
		'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.9.0/codemirror.js',
		'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.9.0/mode/xml/xml.js',
		'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.9.0/mode/htmlmixed/htmlmixed.js',
		static('admin/js/code-editor.js')
	)

# Note - this always goes last
@hooks.register('insert_global_admin_js')
def custom_admin_js():
	return format_html(
		'<script type="text/javascript" src="{}"></script>',
		static('admin/js/custom-admin.js')
	)


# ========== Admin Menu ============

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

@hooks.register('register_rich_text_features')
def register_center_feature(features):
	feature_name = 'center'
	type_ = 'center'
	tag = 'div'

	control = {
		'type':        type_,
		'label':       'C',
		'description': 'Center',
	}

	features.register_editor_plugin(
		'draftail', feature_name, draftail_features.InlineStyleFeature(control)
	)

	features.register_converter_rule('contentstate', feature_name, {
		'from_database_format': {'div[class]': InlineStyleElementHandler(type_)},
		'to_database_format': {
			'style_map': {
				type_: {
					'element': tag,
					'props': {
						'class': 'text-center',
					},
				},
			},
		},
	})

	features.default_features.append(feature_name)
