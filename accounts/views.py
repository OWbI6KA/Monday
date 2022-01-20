from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


def register(request):
    form = CreateUserForm
    if request.method == 'POST':
        _name = request.POST['myName']
        _surname = request.POST['mySurname']
        _email = request.POST['myEmail']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # _access = request.POST['myAccess']

        myUser = User.objects.create_user(_email, _email, password1)
        myUser.first_name = _name
        myUser.last_name = _surname
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
            _name = user.first_name
            return render(request, 'cabinet/index.html', {'myName': _name})

        else:
            messages.error(request, 'Проверьте правильность введенных данных')
            return redirect('accounts:login')

    return render(request, 'accounts/login.html')


def logout_view(request):
    return redirect('accounts : login')
