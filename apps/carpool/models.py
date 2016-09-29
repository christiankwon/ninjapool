from __future__ import unicode_literals
from django.db import models
from ..account.models import User
# from ..wall.models import Wall

# Create your models here.
class CarpoolManager(models.Manager):
    def newcarpool(self, user, room):
        this.create(driver=user, num_passengers=room)

class Carpool(models.Model):
    num_passengers = models.IntegerField()
    arrival_time = models.TimeField()
    leave_time = models.TimeField()
    driver = models.OneToOneField(User)
    # wall = models.OneToOneField(Wall)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CarpoolManager()


class Location(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    user = models.OneToOneField(User)
    route = models.ForeignKey(Carpool)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
