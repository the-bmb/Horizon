from rest_framework import viewsets
from api.serializers import UserSerializer
from api.serializers import FlightSerializer
from api.serializers import TravelersSerializer
from api.serializers import TravelSerializer
from api.models import User
from api.models import Flight
from api.models import Travel
from api.models import Travelers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class TravelersViewSet(viewsets.ModelViewSet):
    queryset = Travelers.objects.all()
    serializer_class = TravelersSerializer


class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
