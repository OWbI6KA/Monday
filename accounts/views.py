from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group

from django.shortcuts import redirect, render

from django.urls import reverse

usersDirectors = Group.objects.get(name='superUsers').user_set.all()


def register(request):
    if request.method == 'POST':
        _name = request.POST['myName']
        _surname = request.POST['mySurname']
        _email = request.POST['myEmail']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Пароли не совпадают")
        elif User.objects.filter(username=_email):
            messages.error(request, "Пользователь с такой почтой уже существует")
        else:
            myUser = User.objects.create_user(_email, _email, password1)
            myUser.first_name = _name
            myUser.last_name = _surname

            # Функция для проверки на руководителя
            if len(request.POST['myAccess']) != 0:
                _access = request.POST['myAccess']
                if _access == '12345':  # Пароль для входа в качестве руководителя
                    _group = Group.objects.get(name='superUsers')
                    myUser.groups.add(_group)

            myUser.save()

            messages.success(request, "Ваш аккаунт был успешно создан")
            return redirect('accounts:login')

    return render(request, 'accounts/register.html')


def login_view(request):
    if request.method == "POST":
        _user = request.POST['myEmail']
        _password = request.POST['myPassword']

        user = authenticate(username=_user, password=_password)

        if user is not None:
            login(request, user)
            if user in usersDirectors:  # Проверка на руководителя
                return redirect(reverse('personal_account:private'))
            else:
                return redirect(reverse('personal_account:general'), )

        else:
            messages.error(request, 'Проверьте правильность введенных данных!')
            return redirect('accounts:login')

    return render(request, 'accounts/login.html')


def logout_view(request):
    auth.logout(request)
    return redirect('home_page:home')
