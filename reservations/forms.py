from django.forms import ModelForm, ValidationError

from .models import Owner


class CreateOwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ("name", "email")
        
    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        
        if len(name) < 3:
            raise ValidationError("Name is too short (must have at least 3 chars)")
        
        return name