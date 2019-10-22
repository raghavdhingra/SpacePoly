from rest_framework import serializers
from .models import *

class CardSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Cards
        fields = '__all__'

class PlayerSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'
