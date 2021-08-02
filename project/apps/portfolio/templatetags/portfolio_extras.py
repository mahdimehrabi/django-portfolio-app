from django import template
from django.utils.translation import get_language

register = template.Library()


@register.simple_tag
def get_translatable_field(obj, field):
    """
    get an object an a translable field that the field with same name and + _fa exist and
    return the value according to current language
    """
    try:
        lang = get_language()
        field = field if lang == 'en' else field + '_fa'
        return getattr(obj, field)
    except AttributeError:
        return None
