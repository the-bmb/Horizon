from django.urls import include, path
from .views import UserList
from .views import UserDetail
from .views import FlightList
from .views import FlightDetail
from .views import TravelersList
from .views import TravelersDetail
from .views import TravelList
from .views import TravelDetail

# from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('flights/', FlightList.as_view()),
    path('flights/<int:pk>/', FlightDetail.as_view()),
    path('travelers/', TravelersList.as_view()),
    path('travelers/<int:pk>/', TravelersDetail.as_view()),
    path('travels/', TravelList.as_view()),
    path('travels/<int:pk>/', TravelDetail.as_view()),
]