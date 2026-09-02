from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import redirect

from .models import Place, Owner, OwnerDocument
from .forms import CreateOwnerForm, CreatePlaceForm, EditOwnerForm, UploadDocumentsForm
from .utils import get_owner_by_id

def main_view(request):
    template = loader.get_template("reservations/main.html")
    rendered = template.render({ }, request)
    return HttpResponse(rendered)

def index(request):
    template = loader.get_template("reservations/index.html")
    place = Place.objects.first()
    rendered = template.render({ "place": place }, request)

    return HttpResponse(rendered)

def place_by_id(request, id):
    try:
        place = Place.objects.get(pk=id)
    except Place.DoesNotExist:
        raise Http404("Place doesnt exist")
        
    template = loader.get_template("reservations/index.html")
    rendered = template.render({ "place": place }, request)
    return HttpResponse(rendered)

def all_places(request):
    min_floor = request.GET.get("min_floor")
    max_floor = request.GET.get("max_floor")
    
    if min_floor is not None and max_floor is not None:
        places = Place.objects.filter(floor__gte=min_floor, floor__lte=max_floor)
    elif min_floor is not None:
        places = Place.objects.filter(floor__gte=min_floor)
    elif max_floor is not None:
        places = Place.objects.filter(floor__lte=max_floor)
    else:
        places = Place.objects.all()
    
    template = loader.get_template("reservations/all_places.html")
    rendered = template.render({ "places": places }, request)

    return HttpResponse(rendered)


def all_owners(request):
    owners = Owner.objects.all()
    template = loader.get_template("reservations/all_owners.html")
    rendered = template.render({ "owners": owners }, request)

    return HttpResponse(rendered)

def owner_by_id(request, id):
    owner = get_owner_by_id(id)
    template = loader.get_template("reservations/one_owner.html")
    
    places = owner.places.all()
    
    rendered = template.render({ "owner": owner, "places": places }, request)
    return HttpResponse(rendered)


def upload_documents(request):
    if request.method == "POST":
        form = UploadDocumentsForm(request.POST, request.FILES)

        if form.is_valid():
            owner = Owner.objects.create(name="No name", email="no_email")

            documents = request.FILES.getlist('documents')
            for doc in documents:
                OwnerDocument.objects.create(
                    owner=owner,
                    file=doc
                )
            
            return redirect("all_owners")
    elif request.method == "GET":
        form = UploadDocumentsForm()
    else:
        return HttpResponseBadRequest("Invalid HTTP method")
    
    template = loader.get_template("reservations/upload_documents.html")
    rendered = template.render({ "form": form }, request)
    return HttpResponse(rendered)


def create_owner(request):
    if request.method == "POST":
        form = CreateOwnerForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("all_owners")
    elif request.method == "GET":
        form = CreateOwnerForm()
    else:
        return HttpResponseBadRequest("Invalid HTTP method")
    
    template = loader.get_template("reservations/create_owner.html")
    rendered = template.render({ "form": form }, request)
    return HttpResponse(rendered)


def edit_owner(request, id):
    owner = get_owner_by_id(id)
    
    if request.method == "POST":
        form = EditOwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect("all_owners")
    elif request.method == "GET":
        form = EditOwnerForm(instance=owner)
    else:
        return HttpResponseBadRequest("Invalid HTTP method")
    
    template = loader.get_template("reservations/edit_owner.html")
    rendered = template.render({ "form": form }, request)
    return HttpResponse(rendered)


def create_place(request):
    if request.method == "POST":
        form = CreatePlaceForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect("all_places")
    elif request.method == "GET":
        form = CreatePlaceForm()
    else:
        return HttpResponseBadRequest("Invalid HTTP method")
    
    template = loader.get_template("reservations/create_place.html")
    rendered = template.render({ "form": form }, request)
    return HttpResponse(rendered)
# Testing

def get_first_owner_places(request):
    owner = Owner.objects.get(pk=1)
    places = owner.places.all()
    return HttpResponse(len(list(places)))

def places_from_expensive(request):
    template = loader.get_template("reservations/all_places.html")
    places = Place.objects.all().order_by('-price')
    rendered = template.render({ "places": places }, request)

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
    address_contains_test = Place.objects.filter(address__contains="place" ) # содержит слово place
    price_more_4_and_room_2 = Place.objects.filter(price__gte=4000000, rooms=2) # оба условия
        
    rendered = template.render( { "places": price_more_4_or_eq }, request)
    return HttpResponse(rendered)

