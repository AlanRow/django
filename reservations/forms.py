from django.forms import ModelForm

from .models import Place


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ("address", "price", "built_at", "rooms", "owner", "floor")
