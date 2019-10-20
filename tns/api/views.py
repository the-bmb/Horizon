from rest_framework import generics
from .serializers import UserSerializer
from .serializers import FlightSerializer
from .serializers import TravelersSerializer
from .serializers import TravelSerializer
from .models import User
from .models import Flight
from .models import Travel
from .models import Travelers


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FlightList(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class TravelersList(generics.ListCreateAPIView):
    queryset = Travelers.objects.all()
    serializer_class = TravelersSerializer


class TravelersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Travelers.objects.all()
    serializer_class = TravelersSerializer


class TravelList(generics.ListCreateAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer


class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
