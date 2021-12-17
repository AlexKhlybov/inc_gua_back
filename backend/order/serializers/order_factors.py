from rest_framework import serializers

from . import OrderListSerializer, FactorsSerializer
from ..models import OrderFactors


class OrderFactorsSerializer(serializers.ModelSerializer):
    order = OrderListSerializer(read_only=True)
    factors = FactorsSerializer(read_only=True)

    class Meta:
        model = OrderFactors
        fields = (
            'order',
            'factors',
            'value',
        )
