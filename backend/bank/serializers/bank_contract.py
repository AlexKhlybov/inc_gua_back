from rest_framework import serializers

from ..models import BankСontract
from bank.serializers.bank import BankSerializer


class BankСontractSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)

    class Meta:
        model = BankСontract
        fields = '__all__'
