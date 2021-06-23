from django.db import models
from django.db.models import Avg, Count
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
import datetime
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator

# Every model gets a primary key field by default.
# Resturants, Users
# User is provided by Django. The email field is not unique by
# default, so add this to prevent more than one user with the same email.
User._meta.get_field('email')._unique = True

#Require email, first name and last name
User._meta.get_field('email')._blank = False
User._meta.get_field('last_name')._blank = False
User._meta.get_field('first_name')._blank = False

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='user_profile_images/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        old_profile = Profile.objects.filter(pk=self.pk).first()
        if old_profile and old_profile.profile_image:
            if old_profile.profile_image != self.profile_image:
                self.delete_image(old_profile.profile_image)

        super().save(*args, **kwargs)

    def delete_image(self, image):
        if default_storage.exists(image.name):
            default_storage.delete(image.name)


    def delete(self, *args, **kwargs):
        if self.profile_image:
            self.delete_image(self.profile_image)

        super().delete(*args, **kwargs)        


    def __str__(self):
        return f'Name: {self.user.first_name}{self.user.last_name}, Email: {self.user.email}, \
          Profile Image: {self.profile_image}, Bio: {self.bio}'


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)

class Resturant(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    direction = models.CharField(max_length=200, blank=False, unique=True)
    hyper_link = models.CharField(max_length=500, blank=False, unique=True)
    hours_open = models.CharField(max_length=200, blank=False, unique=True)
    description = models.CharField(max_length=200, blank=False, unique=True)

    def __str__(self):
        return f'Name: {self.name} /n Direction: {self.direction} /n {self.hyper_link} /n Hours: {self.hours_open} /n Description: {self.description}'