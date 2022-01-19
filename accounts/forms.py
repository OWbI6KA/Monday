from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class myUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['myName', 'mySurname', 'myEmail', 'myPassword1', 'myPassword2', 'myAccess']

    myName = forms.Field(widget=forms.TextInput())
    mySurname = forms.Field(widget=forms.TextInput())
    myEmail = forms.Field(widget=forms.EmailInput())
    myPassword1 = forms.Field(widget=forms.PasswordInput())
    myPassword2 = forms.Field(widget=forms.PasswordInput())
    myAccess = forms.Field(widget=forms.TextInput())

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = instance.myEmail
        if commit:
            instance.save()
        return instance
