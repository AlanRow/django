from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("place/<str:id>", views.place_by_id, name="place_by_id"),
    path("places", views.places_list, name="places")
]