from django.forms import Form, ModelForm,ValidationError, FileField, ClearableFileInput

from .models import Owner, Place

class UploadDocumentsForm(Form):
    documents = FileField(
        widget=ClearableFileInput,
        required=False
    )

class CreateOwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ("name", "email")
        
    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        
        if len(name) < 3:
            raise ValidationError("Name is too short (must have at least 3 chars)")
        
        return name


class EditOwnerForm(CreateOwnerForm):
    pass
    
class CreatePlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = (
            "address",
            "price",
            "built_at",
            "rooms",
            "owner",
            "photo",
        )
        
    def clean_price(self):
        price = self.cleaned_data["price"]
        
        if price <= 0:
            raise ValidationError("Price must be positive")
        
        return price
    