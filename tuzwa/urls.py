from django.conf.urls import url

from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

url(r'^profile_edit/', views.profile_edit,name='edit_profile'),

url(r'^profile/', views.profile, name='profile'),

url(r'^project/(\d+)$', views.single_project, name='single_image'),

url(r'^new_project/', views.new_project, name='new_project'),

url(r'^design/(?P<project_id>\d+)$', views.design, name='design'),

url(r'^content/(?P<project_id>\d+)', views.content, name='content'),

url(r'^creativity/(?P<project_id>\d+)', views.creativity, name='creativity'),

url(r'^usability/(?P<project_id>\d+)', views.usability, name='usability'),

url(r'^search/', views.search_results, name='search_results'),

url(r'^api/project/$', views.ApiProject.as_view()),

url(r'^api/project/post/$', views.PostApiProject.as_view()),

url(r'^api/profile/$', views.ApiProfile.as_view()),

url(r'^api/profile/post/$', views.PostApiProfile.as_view()),

url(r'^api-token-auth/', obtain_auth_token),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)