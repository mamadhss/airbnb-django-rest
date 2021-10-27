from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
    def create(self,validated_data):
        return Room.objects.create(**validated_data)  
    def validate(self,data):
        if self.instance:
            check_in = data.get("check_in",self.instance.check_in)
            check_out = data.get("check_out",self.instance.check_out)  
        else:
            check_in = data.get("check_in")
            check_out = data.get("check_out")  
            if check_in == check_out:
                raise ValidationError('NOT enough time between changes')
        return data        

    def updated(self,instance,validate_data):
        instance.name = validate_data.get("name",instance.name)
        instance.address = validate_data.get("address",instance.address)
        instance.price = validate_data.get("price",instance.price)
        instance.beds = validate_data.get("beds",instance.beds)
        instance.lat = validate_data.get("lat",instance.lat)
        instance.lng = validate_data.get("lng",instance.lng)
        instance.bedrooms =  validate_data.get("bedrooms",instance.bedrooms)
        instance.bathrooms =validate_data.get("bathrooms",instance.bathrooms)
        instance.check_in = validate_data.get("check_in",instance.check_in)
        instance.check_out = validate_data.get("check_out",instance.check_out)
        instance.instant_book = validate_data.get("instant_book",instance.instant_book)

        instance.save()
        return instance



