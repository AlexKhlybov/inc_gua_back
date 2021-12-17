from rest_framework import serializers

from ..models import Limit
from entity.serializers import PrincipalSerializer
from ..serializers import LimitFZSerializer, LimitBankSerializer, LimitPrincipalBaseSerializer


class LimitSerializer(serializers.ModelSerializer):
    principal = PrincipalSerializer(read_only=True)
    limit_fz = LimitFZSerializer(read_only=True)
    limit_bank = LimitBankSerializer(read_only=True)
    limit_principal = LimitPrincipalBaseSerializer(read_only=True)
    delta = serializers.IntegerField()

    class Meta:
        model = Limit
        fields = '__all__'
