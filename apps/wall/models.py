from django.db import models
from ..account.models import User


class WallManager(models.Manager):
    def new_wall(self, user_id, session_id):
        new_wall = self.create()
        new_wall.users.add(user_id, session_id)
        new_wall.save()

        return new_wall

    def create_wall(self, user_id, session_id):
        messager = User.objects.get(id=session_id)
        messagee = User.objects.get(id=user_id)
        walls = Wall.objects.filter(users=messager).filter(users=messagee)

        for wall in walls:
            if wall.users.count() == 2:
                return wall

        return self.new_wall(messager, messagee)


class MessageManager(models.Manager):
    def new_message(self, message, messager, wall_id):
        errors = []

        if len(message) < 1:
            errors.append("Message cannot be blank.")

        if not errors:
            messager = User.objects.get(id=messager)
            wall = Wall.objects.get(id=wall_id)
            message = self.create(message_body=message, messager=messager, walls=wall)
            return (True, message, wall_id)

        else:
            return (False, errors)


class Wall(models.Model):
    users = models.ManyToManyField(User, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WallManager()


class Message(models.Model):
    walls = models.ForeignKey(Wall)
    messager = models.ForeignKey(User)
    message_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()
