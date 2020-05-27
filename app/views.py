import os
from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime as dt


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = dt.datetime.now()
    msg = f'Текущее время: {current_time:%H:%M:%S}'
    return HttpResponse(msg)


def workdir_view(request):
    ls = os.listdir(path=".")
    list_ls = [line+'\t' for line in ls]
    return HttpResponse(list_ls)
