from rest_framework import serializers
from .models import Project, Profile


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model =Project
        fields = ['image', 'image2', 'image3', 'project_name', 'caption', 'description', 'profile', 'user']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar', 'Bio', 'phone_number', 'email']        