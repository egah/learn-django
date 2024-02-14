from django import template

register = template.Library()


#! @register.filter(name="nom_filtre")
#! register.filter("nom_filtre", add_hash)
@register.filter
def add_hash(value, elem):
    return elem + value
