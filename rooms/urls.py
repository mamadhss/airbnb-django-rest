from django.urls import path
from rest_framework import urlpatterns
from . import views

urlpatterns = [
    path("",views.RoomsView.as_view()),
    path("<int:room_id>/",views.RoomView.as_view())
]