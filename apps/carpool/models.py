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
