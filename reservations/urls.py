from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("places", views.all_places, name="all_places"),
    path("places/create", views.create_place, name="create_place"),
    path("places/<str:id>", views.place_by_id, name="place_py_id"),
    path("owners/<str:id>", views.owner_by_id, name="owner_py_id"),
    path("places_exp", views.places_from_expensive, name="places_expensive"),
    path("pars", views.test_search_param, name="test_search_param"),
    path("filtering", views.test_filter_places, name="test_filtering"),
    path("first_owner", views.get_first_owner_places, name="get_first_owner_places"),
]
