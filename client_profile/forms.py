import re

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import ClientUser


class RegisterClientForm(UserCreationForm):
    age = forms.IntegerField(required=True, label="Age")
    location = forms.CharField(max_length=50, label="Location")
    phone = forms.CharField(max_length=11, label="Phone")

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

        if ClientUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Phone is already existed")

        return phone
