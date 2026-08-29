from django import forms
from django.contrib.auth.forms import UserCreationForm
import re

from .models import ClientUser


class RegisterClientForm(UserCreationForm):
    age = forms.IntegerField(min_value=0, label="Age")
    location = forms.CharField(max_length=255, label="Location")
    phone = forms.CharField(max_length=20, label="Phone")

    class Meta:
        model = ClientUser
        fields = (
            "username",
            "age",
            "location",
            "phone",
            "password1",
            "password2",
        )

    def clean_phone(self):
        phone = re.sub(r"[^0-9+]", "", self.cleaned_data["phone"])

        if phone.count("+") > 1 or ("+" in phone and not phone.startswith("+")):
            raise forms.ValidationError("Plus is allowed only once at the beginning")

        if not phone.replace("+", ""):
            raise forms.ValidationError("Enter a phone number")

        if ClientUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Phone is already used")

        return phone
        
