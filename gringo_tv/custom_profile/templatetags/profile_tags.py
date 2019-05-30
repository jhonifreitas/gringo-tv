from django import template

register = template.Library()

@register.filter
def concat(value, concat):
    return str(value) + str(concat)
