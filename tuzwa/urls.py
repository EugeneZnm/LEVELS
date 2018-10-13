from django.conf.urls import url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

url(r'^profile_edit/', views.profile_edit,name='edit_profile'),

url(r'^profile/', views.profile, name='profile'),

url(r'^project/(\d+)', views.single_project, name='single_image'),

url(r'^new_project/', views.new_project, name='new_project'),

url(r'^vote/(?P<project_id>\d+)', views.votes, name='vote'),

url(r'^search/', views.search_results, name='search_results'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)