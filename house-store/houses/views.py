from django.http import HttpRequest
from django.shortcuts import render

from houses.models import House


def houses_list(request: HttpRequest):
    houses = House.objects.all()
    return render(request, 'houses/houses_list.html', {'houses': houses})
