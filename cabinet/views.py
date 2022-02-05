from django.shortcuts import render


def general(request):
    return render(request, 'cabinet/general.html')


def private(request):
    return render(request, 'cabinet/private.html')
