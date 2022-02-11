from django.shortcuts import render
from django.views.generic.list import ListView
from .models import monday_data


def general(request):
    _name = request.user.first_name
    workTask = monday_data.objects.all()
    return render(request, 'cabinet/general.html', {'myName': _name, 'workTask': workTask})


def private(request):
    _name = request.user.first_name
    workTask = monday_data.objects.all()
    return render(request, 'cabinet/private.html', {'myName': _name, 'workTask': workTask})

# class TasksView(ListView):
#     model = monday_data
#     template_name = 'cabinet/general.html'
#     context_object_name = 'work'
