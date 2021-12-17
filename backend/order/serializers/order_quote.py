from rest_framework import serializers

from . import OrderListSerializer, QuoteSerializer
from ..models import OrderQuote


class OrderQuoteSerializer(serializers.ModelSerializer):
    order = OrderListSerializer(read_only=True)
    quote = QuoteSerializer(read_only=True)

    class Meta:
        model = OrderQuote
        fields = ('__all__')
