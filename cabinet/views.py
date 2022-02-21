from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .models import MondayData

_data = MondayData.objects.all()

#Подумать над производительностью
def general(request):
    if request.user.is_authenticated:
        _name = request.user.first_name
        _group1 = Group.objects.get(name='Group_1').user_set.all()
        _group2 = Group.objects.get(name='Group_2').user_set.all()
        _group3 = Group.objects.get(name='Group_3').user_set.all()
        if request.user in _group1:
            _group = 'Group_1'
        elif request.user in _group2:
            _group = 'Group_2'
        elif request.user in _group3:
            _group = 'Group_3'
        return render(request, 'cabinet/general.html', {'myName': _name, 'myData': _data, 'myGroup': _group})
    else:
        return redirect('accounts:login')


def private(request):
    _leaders = Group.objects.get(name='superUsers').user_set.all()
    if request.user.is_authenticated:
        _name = request.user.first_name
        if request.user in _leaders:
            return render(request, 'cabinet/private.html', {'myName': _name, 'myData': _data})
        else:
            return redirect('personal_account:general')
    else:
        return redirect('accounts:login')
