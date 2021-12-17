from rest_framework import serializers

from ..models import OrderFactors


class GetFactorsSerializer(serializers.ModelSerializer):
    description = serializers.CharField()

    class Meta:
        model = OrderFactors
        fields = ['order', 'description']
