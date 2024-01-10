from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from houses.models import House
from orders.forms import OrderForm


def house_detail(request: HttpRequest, house_id: int):
    form = OrderForm()
    house = get_object_or_404(House, id=house_id)

    context = {
        'house': house,
        'form': form,
    }
    template = 'houses/house_detail.html'

    return render(request, template_name=template, context=context)


def houses_list(request: HttpRequest):
    houses = House.objects.all()
    return render(request, 'houses/houses_list.html', {'houses': houses})
