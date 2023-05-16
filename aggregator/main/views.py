from rest_framework import generics
from .models import Hotels, Rooms, Devices, Services, Clients
from .serializers import (ClientsSerializer, HotelsSerializer, RoomsSerializer,
                          DevicesSerializer, ServicesSerializer)
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class HotelsList(generics.ListCreateAPIView):
    permission_classes = IsAdminUser
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer


class HotelsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsAdminUser
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer


class ClientsList(generics.ListCreateAPIView):
    permission_classes = IsAdminUser
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class ClientsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsAdminUser
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class RoomsList(generics.ListCreateAPIView):
    permission_classes = IsAdminUser
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer


class RoomsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsAdminUser
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer


class DevicesList(generics.ListCreateAPIView):
    permission_classes = IsAdminUser
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer


class DevicesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsAdminUser
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer


class ServicesList(generics.ListCreateAPIView):
    permission_classes = IsAuthenticated
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsAuthenticated
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
