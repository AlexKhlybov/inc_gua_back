from rest_framework import serializers

from ..models import BankLimits
from bank.serializers.bank import BankSerializer


class BankLimitsSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)

    class Meta:
        model = BankLimits
        fields = ['id', 'bank', 'total_limit', 'current_guaranties_sum', 'orders_sum', 'free_balance',
                  'create_at', 'update_at']


class BankLimitsUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankLimits
        fields = ['id', 'bank', ]
