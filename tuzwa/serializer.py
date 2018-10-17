from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model =Project
        fields = ('image', 'image2', 'image3', 'project_name', 'caption', 'description', 'profile', 'user')