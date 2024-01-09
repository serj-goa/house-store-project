from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from houses.models import House


def house_detail(request: HttpRequest, house_id: int):
    house = get_object_or_404(House, id=house_id)
    return render(request, 'houses/house_detail.html', {'house': house})


def houses_list(request: HttpRequest):
    houses = House.objects.all()
    return render(request, 'houses/houses_list.html', {'houses': houses})
