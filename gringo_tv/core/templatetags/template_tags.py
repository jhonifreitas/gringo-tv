from django import template

from gringo_tv.custom_profile.models import Indication


register = template.Library()


@register.filter('get_color_status')
def get_color_status(value):
    color = 'dark'
    if Indication.PENDING == value:
        color = 'warning'
    elif Indication.NOT_ACTIVE == value:
        color = 'danger'
    elif Indication.ACTIVE == value:
        color = 'success'
    return color


@register.filter('mask_phone')
def mask_phone(value):
    return '({}) {}-{}'.format(value[0:2], value[2:7], value[7:])


@register.filter('concat')
def concat(value, concat):
    return str(value) + str(concat)
