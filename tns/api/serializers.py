from rest_framework import serializers
from api.models import User
from api.models import Flight
from api.models import Travel
from api.models import Travelers


class Login(serializers.ModelSerializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        read_only_fields = ['id']


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('__all__')
        read_only_fields = ['id']


class TravelersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travelers
        fields = ('__all__')
        read_only_fields = ['id']


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ('__all__')
        read_only_fields = ['id']
