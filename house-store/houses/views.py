from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from houses.models import House
from orders.forms import OrderForm


def house_detail(request: HttpRequest, house_id: int):
    house = get_object_or_404(House, id=house_id)
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
    houses = House.objects.all()
    return render(request, 'houses/houses_list.html', {'houses': houses})
