from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    sort = request.GET.get('sort')
    to_sort = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
        None: 'id',
    }
    template = 'catalog.html'
    context = {
        'phones_list': Phone.objects.all().order_by(to_sort[sort])
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)
