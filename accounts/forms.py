from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['myName', 'mySurname', 'myEmail', 'password1', 'password2', 'myAccess']

    myName = forms.Field(widget=forms.TextInput())
    mySurname = forms.Field(widget=forms.TextInput())
    myEmail = forms.Field(widget=forms.EmailInput())
    myAccess = forms.Field(widget=forms.TextInput())
