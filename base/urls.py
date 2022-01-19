from django.urls import path
from . import views

app_name = 'home_page'
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.support, name='help'),
]