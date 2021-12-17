from rest_framework import serializers

from ..models import Contest
from .lot import LotSerializer
from .contest_type import ContestTypeSerializer
from .contract import ContractSerializer
from limit.serializers.limit_fz import LimitFZSerializer


class ContestSerializer(serializers.ModelSerializer):
    lot = LotSerializer(read_only=True)
    type = ContestTypeSerializer(read_only=True)
    contract = ContractSerializer(read_only=True)
    fz = LimitFZSerializer(read_only=True)

    class Meta:
        model = Contest
        fields = ['id', 'lot', 'type', 'contract', 'defined', 'fz', 'okpd2', 'nmck', 'create_at', 'update_at']
