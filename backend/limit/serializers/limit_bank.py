from rest_framework import serializers

from ..models import LimitBank
from bank.serializers.bank import BankSerializer


class LimitBankSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)

    class Meta:
        model = LimitBank
        fields = ['id', 'bank', 'limit', 'create_at', 'update_at']
