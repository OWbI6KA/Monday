from django.shortcuts import render, redirect
from .models import monday_data
from django.contrib.auth.models import Group

_data = monday_data.objects.all()
_leaders = Group.objects.get(name='superUsers').user_set.all()

def general(request):
    if request.user.is_authenticated:
        _name = request.user.first_name
        return render(request, 'cabinet/general.html', {'myName': _name, 'myData': _data})
    else:
        return redirect('accounts:login')


def private(request):
    if request.user.is_authenticated:
        _name = request.user.first_name
        if request.user in _leaders:
            return render(request, 'cabinet/private.html', {'myName': _name, 'myData': _data})
        else:
            return redirect('personal_account:general')
    else:
        return redirect('accounts:login')
