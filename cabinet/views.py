from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from django.contrib.auth.hashers import check_password
from .models import MainData

_data = MainData.objects.all()


# Подумать над производительностью
def general(request):
    if request.user.is_authenticated:
        _name = request.user.first_name
        _group1 = Group.objects.get(name='Group_1').user_set.all()
        _group2 = Group.objects.get(name='Group_2').user_set.all()
        _group3 = Group.objects.get(name='Group_3').user_set.all()
        if request.user in _group1:
            _group = 'Group_1'
            userGroup = 'Первая бригада'
        elif request.user in _group2:
            _group = 'Group_2'
            userGroup = 'Вторая бригада'
        elif request.user in _group3:
            _group = 'Group_3'
            userGroup = 'Третья бригада'
        full_name = request.user.get_full_name()
        email = request.user.email
        return render(request, 'cabinet/general.html',
                      {'myName': _name, 'myData': _data, 'myGroup': _group, 'userName': full_name, 'email': email,
                       'userGroup': userGroup})
    else:
        return redirect('accounts:login')


def private(request):
    _leaders = Group.objects.get(name='superUsers').user_set.all()
    if request.user.is_authenticated:
        _name = request.user.first_name
        if request.user in _leaders:
            full_name = request.user.get_full_name()
            email = request.user.email
            return render(request, 'cabinet/private.html',
                          {'myName': _name, 'myData': _data, 'userName': full_name, 'email': email})
        else:
            return redirect('personal_account:general')
    else:
        return redirect('accounts:login')


def change_password(request):
    if request.method == 'POST':
        _oldPassword = request.POST['oldPassword']
        _newPassword = request.POST['newPassword1']
        _newPassword2 = request.POST['newPassword2']
        if check_password(_oldPassword, request.user.password):
            myUser = User.objects.get(username=request.user.username)
            if _newPassword == _newPassword2:
                myUser.set_password(_newPassword)
                myUser.save()
                return redirect('user:general')
    return render(request, 'cabinet/change_password.html')
