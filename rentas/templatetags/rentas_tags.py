from django import template

register = template.Library()

@register.simple_tag
def set_temporada():
    return True

@register.simple_tag
def unset_temporada():
    return False
