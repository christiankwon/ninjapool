from __future__ import unicode_literals
from django.db import models
from ..account.models import User, Car
from ..wall.models import Wall

# Create your models here.
class CarpoolManager(models.Manager):
    def new_carpool(self, data):
        user = data['user']

        wall = Wall.objects.create()
        wall.users.add(user)
        wall.save()

        data = {
            'num_passengers': data['seats'],
            'arrival_time': data['arrive'],
            'driver': user,
            'wall': wall,
        }

        create = self.create(**data)

        user.carpool_id = create.id
        user.save()

        print create.id

        return (True, create)

    def leave_carpool(self, user_id):
        user = User.objects.get(id=user_id)
        carpool = self.get(id=user.carpool_id)
        user.carpool_id=0
        user.save()
        if carpool.driver == user:
            carpool.delete()

        return True

    def join_carpool(self, user, carpool_id):
        carpool = self.get(id=carpool_id)
        user.carpool_id=carpool_id
        user.save()

        print carpool.id

        carpool.wall.users.add(user)
        carpool.wall.save()


class Carpool(models.Model):
    num_passengers = models.IntegerField()
    arrival_time = models.TimeField()
    driver = models.OneToOneField(User)
    wall = models.OneToOneField(Wall)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CarpoolManager()
