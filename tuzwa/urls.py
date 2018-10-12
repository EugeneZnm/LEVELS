from django.conf.urls import url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatters = [

url(r'^profile_edit/',views.profile_edit,name='edit_profile'),

]