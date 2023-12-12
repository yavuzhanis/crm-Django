from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Kayit
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User

        fields = ["username", "password1", "password2"]


# Login a user form
class LogınForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


#! create  a record
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Kayit

        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "address",
            "city",
            "province",
            "country",
        ]


#! Update a record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Kayit

        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "address",
            "city",
            "province",
            "country",
        ]
