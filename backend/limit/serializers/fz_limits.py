from rest_framework import serializers

from ..models import FZLimits
from .limit_fz import LimitFZSerializer


class FZLimitsSerializer(serializers.ModelSerializer):
    fz = LimitFZSerializer(read_only=True)

    class Meta:
        model = FZLimits
        fields = ['id', 'fz', 'total_limit', 'current_guaranties_sum', 'orders_sum', 'free_balance',
                  'create_at', 'update_at']


class FZLimitsUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = FZLimits
        fields = ['id', 'fz', ]
