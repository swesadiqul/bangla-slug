from django import template
from django.template.defaultfilters import stringfilter
import markdown as md
from bangla.models import Category


register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])


@register.simple_tag
def get_categories():
    return Category.objects.all()[0:3]