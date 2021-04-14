from django import template

register = template.Library()

@register.filter
def get_item(row, i):
    try:
        return row[i]
    except IndexError:
        return ''

register.filter('filter', get_item)
