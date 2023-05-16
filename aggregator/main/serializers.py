from rest_framework import serializers
from .models import Clients, Hotels, Rooms, Devices, Services


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('client_id',
                  'date_start',
                  'date_end',
                  'room_id')


class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = ('hotel_id',
                  'hotel_name',
                  'city_id')


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('room_id',
                  'room_name',
                  'hotel_id')


class DevicesSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Devices
        fields = ('device_id',
                  'room_id')

    def create(self, validated_data):
        return Devices.objects.create_user(**validated_data)


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('service_id',
                  'service_name',
                  'service_price',
                  'hotel_id')
