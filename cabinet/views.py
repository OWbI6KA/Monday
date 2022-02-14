from django.shortcuts import render, redirect

from .models import monday_data
from accounts.views import usersDirectors


def general(request):
    if request.user.is_authenticated:
        _name = request.user.first_name
        workTask = monday_data.objects.all()
        return render(request, 'cabinet/general.html', {'myName': _name, 'workTask': workTask})
    else:
        return redirect('home_page:home')


def private(request):
    if request.user.is_authenticated and request.user in usersDirectors:
        _name = request.user.first_name
        workTask = monday_data.objects.all()
        return render(request, 'cabinet/private.html', {'myName': _name, 'workTask': workTask})
    else:
        return redirect('home_page:home')
