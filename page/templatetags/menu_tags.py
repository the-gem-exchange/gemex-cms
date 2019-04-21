from django import template

register = template.Library()

@register.simple_tag()
def get_vars(value):
    return vars(value)
