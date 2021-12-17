from rest_framework import serializers

from ..models import Lot


class LotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lot
        fields = '__all__'
