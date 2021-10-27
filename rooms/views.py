from re import I
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Room        
from .serializers import RoomSerializer,BigRoomSerializer


class RoomsView(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class RoomView(generics.RetrieveAPIView):
    serializer_class = BigRoomSerializer
    queryset = Room.objects.all()