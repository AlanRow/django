from django.db import models

class Places(models.Model):
    address = models.CharField(max_length=255)
    price = models.IntegerField()
    

