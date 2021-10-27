from rest_framework import serializers

import rooms
from .models import Room
from users.serializers import TinyUserSerializer

class ReadRoomSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer()

    class Meta:
        model = Room
        exclude = ('modified',)

class WriteRoomSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Room
        exclude = ('modified',)

