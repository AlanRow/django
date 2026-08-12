from datetime import date
from django.db import models

class Place(models.Model):
    address = models.CharField(max_length=255)
    price = models.FloatField()
    built_at = models.DateField(default=date.today)
    rooms = models.IntegerField()
    owner = models.CharField(max_length=50, null=True)
    floor = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.address} ({self.rooms} комнат)'
    

class Car(models.Model):
    make = models.CharField(max_length=50)
    velocity = models.FloatField()

class Person(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField()
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="passengers"
    )
    

