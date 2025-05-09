from django import template

register = template.Library()

@register.filter
def percentage(value, total):
    try:
        value = float(value)
        total = float(total)
        if total == 0:
            return 0
        return (value / total) * 100
    except (ValueError, TypeError):
        return 0
