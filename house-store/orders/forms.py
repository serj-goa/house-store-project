from django import forms as f

from orders.models import Order


class OrderForm(f.ModelForm):
    class Meta:
        model = Order
        fields = 'house', 'name', 'phone'
