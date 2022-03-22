from cmath import pi
from django.contrib import admin
from .models import  menu, item, topping, pizza, place, restaurant
# Register your models here.

admin.site.register(menu)
admin.site.register(item)
admin.site.register(topping)
admin.site.register(pizza)
admin.site.register(place)
admin.site.register(restaurant)