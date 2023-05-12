from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (ClientsList, ClientsDetail, HotelsList, HotelsDetail, RoomsList, RoomsDetail,
                    DevicesList, DevicesDetail, ServicesList, ServicesDetail)

urlpatterns = [
    path("api/clients/", ClientsList.as_view()),
    path("api/clients/<int:pk>/", ClientsDetail.as_view()),
    path("api/hotels/", HotelsList.as_view()),
    path("api/hotels/<int:pk>/", HotelsDetail.as_view()),
    path("api/rooms/", RoomsList.as_view()),
    path("api/rooms/<int:pk>/", RoomsDetail.as_view()),
    path("api/services/", ServicesList.as_view()),
    path("api/services/<int:pk>/", ServicesDetail.as_view()),
    path("api/devices/", DevicesList.as_view()),
    path("api/devices/<int:pk>/", DevicesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
