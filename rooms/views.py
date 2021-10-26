from re import I
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


class RootAPIView(APIView):
    def get(self,request):
        return Response({
            "Hello":"Django"
        })


@api_view(["GET"])
def RootFunc(request):
    return Response({
        'test':'func'
    })        