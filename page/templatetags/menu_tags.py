from django import template

from bs4 import BeautifulSoup # Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import re

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
