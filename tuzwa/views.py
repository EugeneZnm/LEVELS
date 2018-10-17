from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm

# importing login as auth_login to prevent clashing with inbuilt view
from django.contrib.auth import login as auth_login

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# import forms
from .forms import SignUpForm, EditProfileForm,DesignForm, UsabilityForm, UploadProjectForm, CreativityForm,ContentForm

# importation of model classes
from .models import Project,Profile, Design, Usability,Creativity,Content

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer
# Create your views here.


# Home view function
def Home(request):
    projects = Project.show_projects()
    return render(request, 'home.html', {'projects': projects})


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


# edit profile view function
@login_required(login_url='/registration/login/')
def profile_edit(request):
    """
    view function to render profile

    """
    form = EditProfileForm()
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=current_user.profile)
        if form.is_valid():
            form.save()

            return redirect('profile')

    return render(request, 'Profile/profile_edit.html', {'form': form})


# profile view function
@login_required(login_url='/registration/login/')
def profile(request):
    """
    view function to render profile

    """
    current_user = request.user
    profile = Profile.objects.get(user = request.user)
    projects = Project.objects.filter(user = current_user)
    return render(request, 'Profile/profile.html', {'profile': profile, 'projects': projects})


# view function for uploading new project
@login_required(login_url='/registration/login/')
def new_project(request):
    current_user = request.user

    if request.method == 'POST':
        upform = UploadProjectForm(request.POST, request.FILES)
        if upform.is_valid():

            new_image = upform.save( commit=False )
            new_image.user = current_user
            upform.save()
        return redirect('profile')
    else:
        upform = UploadProjectForm()

    return render(request, 'Profile/new_project.html', {"upform": upform})


def single_project(request, project_id):
    """
    function to display single project and voting citeria
    """
    # view function for single project
    projects = Project.single_project(project_id)

    # voting criteria
    # designs = Design.object.all()

    design = Design.objects.all()
    usability = Usability.objects.all()
    creativity = Creativity.objects.all()
    content = Content.objects.all()

    return render(request, 'Profile/single-project.html', {"projects": projects, "project_id": project_id, "design":design, "usability":usability, "creativity":creativity, "content":content})


# criteria voting function
@login_required(login_url='/registration/login/')
def design(request, project_id):

    projects = get_object_or_404(Project, pk=project_id)
    print(projects)
    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            design = form.save(commit=False)
            design.user = request.user
            design.project = projects
            design.save()
        return redirect('single_image', project_id)


@login_required(login_url='/registration/login/')
def usability(request, project_id):

    projects = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = UsabilityForm(request.POST)
        if form.is_valid():
            usability = form.save(commit=False)
            usability.user = request.user
            usability.project = projects
            usability.save()
        return redirect('single_image', project_id)


@login_required(login_url='/registration/login/')
def creativity(request, project_id):

    projects = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = CreativityForm(request.POST)
        if form.is_valid():
            creativity = form.save(commit=False)
            creativity.user = request.user
            creativity.project = projects
            creativity.save()
        return redirect('single_image', project_id)


@login_required(login_url='/registration/login/')
def content(request, project_id):

    projects = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.user = request.user
            content.project = projects
            content.save()
        return redirect('single_image', project_id)


# search project
def search_results(request):
    """
    function to search for projects by project name
    """
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.objects.filter(project_name=search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "project":searched_projects})
    else:
        message = "Enter Project Name to search for"
        return render(request, "search.html", {"message":message})

class Project(APIView):
    def get(self,request,format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)