from django import template


register = template.Library()


@register.filter(name='100_minutes_rate')
def _minus(value):
    return round(value * 100, 3)
