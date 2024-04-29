from django.contrib.auth.models import User
from django.db import models

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0)
    points = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username
