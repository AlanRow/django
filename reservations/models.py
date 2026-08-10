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
    
    
# Практика 1
#  Добавьте в класс Place поле built_at
#  типа DateField с датой сдачи 
#  в эксплуатацию здания / квартиры
#  и поле rooms (IntegerField) с 
#  количеством комнат
#  Примените изменения к базе данных
#  (makemigrations + migrate)

    

