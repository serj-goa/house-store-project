from django.db.models import Q
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from houses.forms import HousesFilterForm
from houses.models import House
from orders.forms import OrderForm


def house_detail(request: HttpRequest, house_id: int):
    house = get_object_or_404(House, id=house_id, active=True)
    form = OrderForm(request.POST or None, initial={'house': house})

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            url = reverse('house_detail', kwargs={'house_id': house.id})

            return HttpResponseRedirect(f'{url}?sent=1')

    context = {
        'house': house,
        'form': form,
        'sent': request.GET.get('sent'),
    }
    template = 'houses/house_detail.html'

    return render(request, template_name=template, context=context)


def houses_list(request: HttpRequest):
    houses = House.objects.filter(active=True)
    form = HousesFilterForm(request.GET)

    if form.is_valid():
        if form.cleaned_data['min_price']:
            houses = houses.filter(price__gte=form.cleaned_data['min_price'])

        if form.cleaned_data['max_price']:
            houses = houses.filter(price__lte=form.cleaned_data['max_price'])

        if form.cleaned_data['query']:
            houses = houses.filter(
                Q(description__icontains=form.cleaned_data['query']) | Q(name__icontains=form.cleaned_data['query'])
            )

        if form.cleaned_data['ordering']:
            houses = houses.order_by(form.cleaned_data['ordering'])

    context = {
        'houses': houses,
        'form': form,
    }
    template = 'houses/houses_list.html'

    return render(request, template_name=template, context=context)
