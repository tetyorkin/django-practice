from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import csv

from app import settings


def index(request):
    return redirect(reverse(bus_stations))


def read_csv():
    all_stations = []
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            bus_stations = {'Name': row['Name'],
                            'Street': row['Street'],
                            'District': row['District']}
            all_stations.append(bus_stations)
    return all_stations


def bus_stations(request):
    page = int(request.GET.get('page', 1))
    paginator = Paginator(read_csv(), 10)
    page_number = paginator.get_page(page)
    if page_number.has_previous():
        prev_page_url = f'?page={page_number.previous_page_number()}'
    else:
        prev_page_url = ''
    if page_number.has_next():
        next_page_url = f'?page={page_number.next_page_number()}'
    else:
        next_page_url = ''
    return render_to_response('index.html', context={
        'bus_stations': page_number.object_list,
        'current_page': page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
