from __future__ import unicode_literals

from django.db import models

from ..account.models import User

# Create your models here.
class MessageManager(models.Manager):
    def add(self, message, messager, messagee):
        if message = '':
            return False
        else:
            self.create(message=message, messager=messager, messagee=mesagee)
            return True


class CarpoolManager(models.Manager):
    def newcarpool(self, user, room):
        this.create(driver=user, num_passengers=room)


class Location(models.Model)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    user = models.OneToOneField(User)
    route = models.ForeignKey(Carpool)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Wall(models.Model):
    users = ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    message = models.CharField(max_length=300)
    author = models.ForeignKey(User)
    wall = models.ForeignKey(Wall)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()


class Carpool(models.Model):
    num_passengers = models.IntegerField()
    arrival_time = models.TimeField()
    leave_time = models.TimeField()
    driver = models.OneToOneField(User)
    wall = models.OneToOne(Wall)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CarpoolManager()
