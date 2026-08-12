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

def test_filter_places(request):
    template = loader.get_template("reservations/all_places.html")
    rooms_2_places = Place.objects.filter(rooms=2) # Ровно 2 комнаты
    price_more_4_or_eq = Place.objects.filter(price__gte=4000000) # больше или равно 4 млн
    price_less_5 = Place.objects.filter(price__lt=5000000) # меньше или равно 5 млн
    address_contains_test = Place.objects.filter(address__contains="place") # сожержит слово place
        
    rendered = template.render( { "places": price_more_4_or_eq }, request)
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
    

