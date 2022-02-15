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
    if request.user.is_authenticated:
        _name = request.user.first_name
        workTask = monday_data.objects.all()
        if request.user in usersDirectors:
            return render(request, 'cabinet/private.html', {'myName': _name, 'workTask': workTask})
        else:
            return redirect('personal_account:general')
    else:
        return redirect('home_page:home')
