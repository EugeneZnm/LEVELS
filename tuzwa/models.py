from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    """
    method to create profile
    """
    avatar = models.ImageField(upload_to='media/', null=True)
    Bio = models.CharField(max_length=2000)
    # deletion of profile and user when deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    location = models.CharField(max_length=200)
    phone_number = models.IntegerField(default=0)
    email = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username

    # sender is source of signal
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        """
        method to create profile
        :return:
        """
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """
        method to save profile
        :return:
        """
        instance.profile.save()


# adding the project profile
class Project(models.Model):
    """
    Project model creating table
    """
    image = models.ImageField(upload_to='media', blank=True)
    image2 = models.ImageField(upload_to='media', blank=True)
    image3 = models.ImageField(upload_to='media', blank=True)
    project_name = models.CharField(max_length=200)
    caption = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE, default=True)

    def save_project(self):
        """
        method to save project images
        :return:
        """
        self.save()

    @classmethod
    def get_project(cls, project_id):
        """
        method to get image by id
        :return:
        """
        projects = cls.objects.filter(id=project_id)
        return projects

    @classmethod
    def show_projects(cls):
        """
        method to get  all images
        :return:
        """
        projects = cls.objects.all()
        return projects

    @classmethod
    def single_project(cls, project_id):
        """
        method to get projects by id
        :return:
        """
        projects = cls.objects.filter(id=project_id)
        return projects

    @classmethod
    def search_by_project_name(cls, search_term):
        """
        method to search for project by name
        :return:
        """
        project = cls.objects.filter(project_name=search_term)
        return project

    def delete_project(self):
        """
        method to delete image
        :return:
        """
        self.delete()


# models for voting criterion
class Votes(models.Model):
    """
    model for design measure criterion
    """
    design = models.IntegerField()
    usability= models.IntegerField()
    creativity = models.IntegerField()
    content = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='votes', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


# class Design(models.Model):
#     """
#     model for design measure criterion
#     """
#     design_score = models.IntegerField()
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='design', null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#
#
# class Usability(models.Model):
#     """
#     model for usability
#     """
#     usability_score = models.IntegerField()
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='usability', null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#
#
# class Creativity(models.Model):
#     """
#     model for scoring creativity
#     """
#     creativity_score = models.IntegerField()
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='creativity', null=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
#
#
# class Content(models.Model):
#     """
#     model for scoring content
#     """
#     content_score =models.IntegerField()
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='content', null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)