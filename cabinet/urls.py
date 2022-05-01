from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('general/', views.general, name='general'),
    path('private/', views.private, name='private')
]
