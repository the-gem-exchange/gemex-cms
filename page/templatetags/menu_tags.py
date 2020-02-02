from django import template

from bs4 import BeautifulSoup # Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

register = template.Library()

@register.simple_tag()
def get_vars(value):
    return vars(value)

@register.simple_tag()
def get_dir(value):
    return dir(value)

@register.filter()
def sex(value):
	if value == 'm':
		return 'Male'
	if value == 'f':
		return 'Female'
	if value == 'x':
		return 'Unisex'
	return ''

@register.simple_tag()
def map_node_html(html, image=None):

	soup = BeautifulSoup(html+"</div>", 'html5lib')
	div  = soup.div
	attrs = div.attrs

	if image:
		attrs['style'] = attrs['style'] + "; background-image:url('" + image.file.url + "');"
		print(attrs['style'])

	return {
		'coords': html,
		'attrs':  attrs
	}
