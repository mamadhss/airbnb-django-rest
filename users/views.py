from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from .serializers import TinyUserSerializer
from users import serializers

class MeAPIView(APIView):
    def get(self,request):
        user = self.request.user
        serializer = TinyUserSerializer(user)
        return Response(serializer.data)

    def put(self,request):
        user = self.request.user
        serializer = TinyUserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(["GET"])
def user_detail(request,user_id):
    try:
        user = User.objects.get(id=user_id)
        serializer = TinyUserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    