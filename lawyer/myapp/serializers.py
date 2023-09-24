from rest_framework import serializers
from .models import Lawyer,City,State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = "__all__"