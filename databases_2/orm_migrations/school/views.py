from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    ordering = 'group'
    template = 'school/students_list.html'
    context = {
        'object_list': Student.objects.all().prefetch_related('teacher').order_by(ordering)
    }
    return render(request, template, context)
