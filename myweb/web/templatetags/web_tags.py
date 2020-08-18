from django import template

register = template.Library()

from ..models  import Buy,Customer,Product