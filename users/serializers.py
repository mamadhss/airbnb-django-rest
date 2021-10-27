from rest_framework import serializers
from .models import User

class TinyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("superhost","username","first_name","last_name","avatar","id",)