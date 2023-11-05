from django import template

register = template.Library()

@register.filter(name='abbreviate')
def abbreviate(value, arg):
    """
    Abbreviates a string to a specified length and adds an ellipsis.
    Usage: {{ your_text|abbreviate:30 }}
    """
    try:
        length = int(arg)
    except ValueError:  # invalid literal for int()
        return value  # Fail silently.

    if not isinstance(value, str):
        value = str(value)

    if len(value) > length:
        return value[:length] + '...'
    else:
        return value