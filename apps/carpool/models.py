from __future__ import unicode_literals
from django.db import models
from ..account.models import User, Car
from ..wall.models import Wall

# Create your models here.
class CarpoolManager(models.Manager):
    def new_carpool(self, data, user_id):
        user = User.objects.get(id=user_id)

        wall = Wall.objects.create()
        wall.users.add(user)
        wall.save()

        data = {
            'num_passengers': data['seats'],
            'arrival_time': data['arrive'],
            'leave_time': data['leave'],
            'max_extra_distance': data['distance'],
            'driver': user,
            'wall': wall,
        }

        create = self.create(**data)

        user.carpool_id = create.id
        user.save()

        return (True, create)


class Carpool(models.Model):
    driver = models.OneToOneField(User)
    wall = models.OneToOneField(Wall)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CarpoolManager()
