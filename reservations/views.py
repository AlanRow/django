from django.http import HttpResponse
from django.template import loader

from .models import Place

def index(request):
    template = loader.get_template("reservations/index.html")
    place = Place.objects.first()
    rendered = template.render({ "place": place }, request)

    return HttpResponse(rendered)

def test_search_param(request):
    template = loader.get_template("reservations/test_search_param.html")
    search_param = request.GET.get("test")
    rendered = template.render({ "param": search_param })
    return HttpResponse(rendered)

def all_places(request):
    template = loader.get_template("reservations/all_places.html")
    places = Place.objects.all()
    rendered = template.render({ "places": places }, request)

    return HttpResponse(rendered)


def places_from_expensive(request):
    template = loader.get_template("reservations/all_places.html")
    places = Place.objects.all().order_by('-price')
    rendered = template.render({ "places": places }, request)

    return HttpResponse(rendered)
    

