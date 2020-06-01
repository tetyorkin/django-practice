from collections import Counter

from django.http import HttpResponse
from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()


def index(request):
    response = request.GET.get('from-landing')
    if response == 'original':
        counter_click['original'] += 1
    elif response == 'test':
        counter_click['test'] += 1
    return render_to_response('index.html')


def landing(request):
    response = request.GET.get('ab-test-arg')
    if response == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')
    elif response == 'original':
        counter_show['original'] += 1
        return render_to_response('landing.html')
    return render_to_response('landing.html')


def stats(request):
    if counter_show['original'] == 0 or counter_show['test'] == 0:
        msg = 'Просмотров не было'
        return HttpResponse(msg)
    test_conversion = counter_click['test'] / counter_show['test']
    original_conversion = counter_click['original'] / counter_show['original']
    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
