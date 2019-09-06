from django import template
from Product.models import Cart
register = template.Library()

@register.filter
def cart_list_amount(cart):
    count = Cart.objects.all().count()
    context = {'pAmount': count}
    return context.get('pAmount')