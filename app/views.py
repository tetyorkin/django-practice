import os
from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime as dt


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': '',
        'Показать содержимое рабочей директории': ''
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = dt.datetime.now()
    msg = f'Текущее время: {current_time:%H:%M:%S}'
    return HttpResponse(msg)


def workdir_view(request):
    ls = os.listdir(path=".")
    list_ls = [line+'\t' for line in ls]
    return HttpResponse(list_ls)
