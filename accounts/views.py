from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import myUser


def register(request):
    form = myUser()

    if request.method == 'POST':
        form = myUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{form.cleaned_data["email"]} registered successfully!')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_view(request):
    context = {}
    return render(request, 'accounts/login.html')


def logout_view(request):
    return redirect('login')
