from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value, arg):
    censor_words = ['fuck', 'suck', 'dick', 'sex']
    if value in censor_words:
        return str('*' * arg)
    else:
        return value

