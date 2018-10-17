from django.contrib import admin
from .models import Project, Profile, Design, Content, Creativity, Usability

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Creativity)
admin.site.register(Usability)
admin.site.register(Content)
admin.site.register(Design)