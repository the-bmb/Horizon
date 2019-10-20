from rest_framework import serializers
from api.models import User
from api.models import Flight
from api.models import Travel
from api.models import Travelers


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'updated_at')


class FlightSerializer(serializers.Serializer):
    class Meta:
        model = Flight
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'updated_at')


class TravelersSerializer(serializers.Serializer):
    class Meta:
        model = Travelers
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'updated_at')


class TravelSerializer(serializers.Serializer):
    class Meta:
        model = Travel
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'updated_at')
