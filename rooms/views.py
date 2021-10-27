from re import I
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics,status
from .models import Room        
from .serializers import ReadRoomSerializer,WriteRoomSerializer


class RoomsView(APIView):
    def post(self,request):
        serializer = WriteRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    
    def get(self,request):
        rooms = Room.objects.all()
        serializer = ReadRoomSerializer(rooms,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
