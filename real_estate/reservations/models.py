from datetime import date
from django.db import models

class Places(models.Model):
    address = models.CharField(max_length=255)
    price = models.FloatField()
    built_at = models.DateField(default=date.today)
    rooms = models.IntegerField()
    
    
# Практика 1
#  Добавьте в класс Places поле built_at
#  типа DateField с датой сдачи 
#  в эксплуатацию здания / квартиры
#  и поле rooms (IntegerField) с 
#  количеством комнат
#  Примените изменения к базе данных
#  (makemigrations + migrate)

    

