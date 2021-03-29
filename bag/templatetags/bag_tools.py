from django import template

register = template.Library()


# Link in messages
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
