from django import template
from taskapp.models import *

register = template.Library()

# @register.simple_tag
# def tasks_open():
#   return Task.objects.filter(status=False)


@register.simple_tag
def tasks_close():
    return Task.objects.filter(status=True)
