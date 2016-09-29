from django.db import models
from ..account.models import User

class WallManager(models.Manager):
    def new_message(self, message, messager,messagee):
        errors=[]
        if len(message) < 1:
            errors.append("Message cannot be blank.")
            return (False, message)
        else:
            self.create(message=message, messager=messager, messagee=mesagee)
            return True

class Wall(models.Model):
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WallManager()
