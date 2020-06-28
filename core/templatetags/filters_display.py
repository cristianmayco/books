from django import template

register = template.Library()


def list_display(self):
    return ', '.join(self)


register.filter('list_display', list_display)
