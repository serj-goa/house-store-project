from django.contrib import admin as a

from orders.models import Order


@a.register(Order)
class OrderAdmin(a.ModelAdmin):
    list_display = 'name', 'phone', 'house', 'date'
