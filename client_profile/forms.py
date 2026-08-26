from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import ClientUser


# Практика: реализовать форму регистрации нового пользователя
# с возможностью задать поля location, phone, age

class RegisterClientForm(UserCreationForm):
    
    class Meta:
        model = ClientUser
        fields = (
            "username",
            "password1",
            "password2",
        )
        
        