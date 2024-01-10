from django import forms as f

from houses.models import House
from orders.models import Order


class OrderForm(f.ModelForm):
    house = f.ModelChoiceField(queryset=House.objects.all(), widget=f.HiddenInput)
    personal_data = f.BooleanField(label='I agree to the processing of personal data', required=True)

    class Meta:
        model = Order
        fields = 'house', 'name', 'phone'
