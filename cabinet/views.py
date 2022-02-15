from django.shortcuts import render, redirect

from .models import monday_data
from accounts.views import usersDirectors

_data = monday_data.objects.all()


def general(request):
    if request.user.is_authenticated:
        _name = request.user.first_name
        return render(request, 'cabinet/general.html', {'myName': _name, 'myData': _data})
    else:
        return redirect('home_page:home')


def private(request):
    if request.user.is_authenticated:
        _name = request.user.first_name
        if request.user in usersDirectors:
            return render(request, 'cabinet/private.html', {'myName': _name, 'myData': _data})
        else:
            return redirect('personal_account:general')
    else:
        return redirect('home_page:home')
