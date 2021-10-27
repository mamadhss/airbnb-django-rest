from django.urls import path
from rest_framework import views
from . import views
app_name = "users"

urlpatterns = [
    path("me/",views.MeAPIView.as_view()),
    path("<int:user_id>/",views.user_detail)
]
