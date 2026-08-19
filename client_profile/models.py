from django.db import models
from django.contrib.auth.models import AbstractUser

class ClientUser(AbstractUser):
    age = models.IntegerField(null=True)
    location = models.CharField(null=True)
    
    def __str__(self):
        return self.username