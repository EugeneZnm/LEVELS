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

