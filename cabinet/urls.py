from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('general/', views.general, name='general'),
    path('private/', views.private, name='private'),
    path('change_password/', views.change_password, name='change_password')
]
