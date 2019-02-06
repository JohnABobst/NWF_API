from rest_framework import serializers
from game.models import *

class MagicCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'
