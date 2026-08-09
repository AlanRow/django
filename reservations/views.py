from django.http import HttpResponse, Http404
from django.template import loader

from .models import Place

def index(request):
    return HttpResponse("Hello, World!")

def place_by_id(request, id):
    try:
        place = Place.objects.get(pk=id)
    except Place.DoesNotExist:
        raise Http404("Place doesnt exists")

    template = loader.get_template("reservations/places_one.html")
    return HttpResponse(template.render({ "place": place }, request))


def places_list(request):
    places = Place.objects.all()

    template = loader.get_template("reservations/places_list.html")
    return HttpResponse(template.render({ "places": places }, request))