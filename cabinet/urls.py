from django.urls import path
from . import views

app_name = 'personal_account'
urlpatterns = [
    path('general', views.general, name='general'),
    path('private', views.private, name='private'),
]
