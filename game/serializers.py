from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('game_id', 'width', 'height', 'mines_count', 'field', 'completed')
