from django.http import HttpResponse
from django.template import loader

from .models import Place

def index(request):
    template = loader.get_template("reservations/index.html")
    place = Place.objects.first()
    rendered = template.render({ "place": place }, request)

    return HttpResponse(rendered)
    

