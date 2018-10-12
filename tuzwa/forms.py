from django import forms

from django.forms import ModelForm, ImageField, TextInput, IntegerField

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Profile, Project, Design, Creativity, Content, User


class SignUpForm(UserCreationForm):
    """
    user creation form for sigup, adding custom field to signup form

    """
    email = forms.CharField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']