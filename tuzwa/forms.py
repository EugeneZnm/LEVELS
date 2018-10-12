from django import forms

from django.forms import ModelForm, ImageField, TextInput, IntegerField

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Profile, Project, Design, Creativity, Content, User


# signup form adding custom field
class SignUpForm(UserCreationForm):
    """
    user creation form for sigup, adding custom field to signup form

    """
    email = forms.CharField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']


# Form for editing profile
class EditProfileForm(forms.ModelForm):
    """
    form for editing profile
    """
    class Meta:
        model = Profile
        fields = ['avatar', 'Bio', 'location', 'phone_number']


# form for uploading new project
class UploadProjectForm(forms.ModelForm):
    """
    form for uploading new project
    """
    class Meta:
        model = Project
        fields = ['image','image2', 'image3', 'project_name', 'caption', 'description']


# form for voting for  design
class DesignForm(forms.ModelForm):
    """
    Vote fon design
    """
    class Meta:
        model = Design
        fields = ['design_score']


# voting on Usability
class UsabilityForm(forms.ModelForm):
    """
    Vote fon design
    """
    class Meta:
        model = Design
        fields = ['usability_score']


# voting on Usability
class CreativityForm(forms.ModelForm):
    """
    Vote fon design
    """
    class Meta:
        model = Design
        fields = ['creativity_score']


# voting on Content
class ContentForm(forms.ModelForm):
    """
    Vote fon design
    """
    class Meta:
        model = Design
        fields = ['content_score']