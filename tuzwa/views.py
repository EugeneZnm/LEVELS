from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404

# importing login as auth_login to prevent clashing with inbuilt view
from django.contrib.auth import login as auth_login

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# import forms
from .forms import SignUpForm

# importation of model classes
from .models import Project,Profile, Design, Content, Creativity, Usability

# Create your views here.


# SIGNUP VIEW FUNCTION
def signup(request):
    """
    signup form view function
    """
    # checking if request method is a post
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # form validationq
        if form.is_valid():
            # saving user credentials and creating uer instance  if form is valid
            user = form.save()

            # user passed as argument to auth_login function
            auth_login(request, user)
            return redirect('edit_profile')
    else:
        form = SignUpForm()

    return render(request, 'registration/registration_form.html', {'form': form})
