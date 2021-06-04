from django.db import models

# Create your models here.

class Resturant(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    direction = models.CharField(max_length=200, blank=False, unique=True)
    hyper_link = models.CharField(max_length=500, blank=False, unique=True)
    hours_open = models.CharField(max_length=200, blank=False, unique=True)
    description = models.CharField(max_length=200, blank=False, unique=True)

    def __str__(self):
        return f'Name: {self.name} /n Direction: {self.direction} /n {self.hyper_link} /n Hours: {self.hours_open} /n Description: {self.description}'