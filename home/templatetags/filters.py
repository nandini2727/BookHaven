from django import template
from babel.numbers import format_currency
register=template.Library()

@register.filter
def mul(value,arg):
    try:
        return float(value)*float(arg)
    except ValueError:
        return ""

@register.filter
def apply_discount(value,arg):
    try:
        return float(value) - (float(value) * float(arg) / 100)
    except:
        return ""
    
@register.filter
def first_author(value, delimiter=","):
    """Return the first part of a string split by the specified delimiter."""
    if value and isinstance(value, str):
        return value.split(delimiter)[0]
    return value

@register.filter
def format_inr(amount):
    return format_currency(amount, 'INR', locale='en_IN')