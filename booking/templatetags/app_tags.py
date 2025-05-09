from django import template
from datetime import date, timedelta

register = template.Library()

@register.simple_tag
def todays_date():
    return date.today().isoformat()

@register.simple_tag
def tommorow():
    return (date.today() + timedelta(days=1)).isoformat()

@register.simple_tag
def max_date():
    return (date.today() + timedelta(days=365)).isoformat()
