from rest_framework import generics
from .models import Clients
from .serializers import ClientsSerializer


class ClientsList(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
