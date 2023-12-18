from django import template
import math

register = template.Library()

# tags - Prosess discount
@register.simple_tag
def cal_sellprice(price, discount):
    if discount is None or discount == 0:
        return math.floor(price)
    return math.floor(price * (100 - discount) / 100)

# filters - Show NTD
@register.filter
def ntd(price):
    return f"{price} NTD"