from django.shortcuts import render
from django.views.generic.list import ListView
from .models import monday_data


def general(request):
    x1 = monday_data.objects.all()
    print(x1)
    return render(request, 'cabinet/general.html', {"tasks": x1})


def private(request):
    return render(request, 'cabinet/private.html')


class TasksView(ListView):
    model = monday_data
    template_name = 'cabinet/general.html'
    context_object_name = 'work'
