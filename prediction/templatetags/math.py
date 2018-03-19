from django import template


register = template.Library()


@register.filter(name='100_minutes_rate')
def _minus(value, args):
    return round(value * args, 3)
