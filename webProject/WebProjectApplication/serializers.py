from rest_framework import serializers
from .models import Tovar
from .models import Room

class TovarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tovar
        fields = ('id', 'name', 'edizm', 'kodkategorii')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')

