from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClientsList, ClientDetail

urlpatterns = [
    path("api/clients/", ClientsList.as_view()),
    path("api/clients/<int:pk>/", ClientDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
