from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from .models import Room        
from .serializers import ReadRoomSerializer,WriteRoomSerializer


class RoomsView(APIView):
    def post(self,request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WriteRoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(user=self.request.user)
            room_serializer = ReadRoomSerializer(room)
            return Response(room_serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    
    def get(self,request):
        rooms = Room.objects.all()
        serializer = ReadRoomSerializer(rooms,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class RoomView(APIView):

    def get(self,request,room_id):
        try:
            room = Room.objects.get(id=room_id)
            serializer = ReadRoomSerializer(room)
            return Response(serializer.data)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    

    def put(self,request,room_id):
        room = Room.objects.get(id=room_id)
        serializer = WriteRoomSerializer(room,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors)    

    def delete(self,request,room_id):
        room = Room.objects.get(id=room_id)
        if room:
            room.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)