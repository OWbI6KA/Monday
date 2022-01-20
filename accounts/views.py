from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


def register(request):
    form = CreateUserForm
    if request.method == 'POST':
        myName = request.POST['myName']
        mySurname = request.POST['mySurname']
        myEmail = request.POST['myEmail']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # myAccess = request.POST['myAccess']

        myUser = User.objects.create_user(myEmail, myEmail, password1)
        myUser.first_name = myName
        myUser.last_name = mySurname

        myUser.save()
        messages.success(request, "Ваш аккаунт был успешно создан")
        return redirect('accounts:login')
    return render(request, 'accounts/register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        myPassword = request.POST['pass1']

        user = authenticate(username=username, password=myPassword)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'accounts/index.html', {'fname': fname})

        else:
            messages.error(request, 'Bad Credentials')
            return redirect('home_page:home')
    return render(request, 'accounts/login.html')


def logout_view(request):
    return redirect('accounts : login')
