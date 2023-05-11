from rest_framework import serializers
from .models import Clients


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('client_id',
                  'date_start',
                  'date_end',
                  'room_id')
