from django.forms import ModelForm

from .models import Owner


class CreateOwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ("name", "email")