from rest_framework import serializers
from magic_card.models import *

class MagicCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = MagicCard
        fields = '__all__'
