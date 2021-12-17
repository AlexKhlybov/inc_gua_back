from rest_framework import serializers

from ..models import Contract
from .purchase import PurchaseSerializer
from entity.serializers.beneficiary import BeneficiarySerializer


class ContractSerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer(read_only=True)
    beneficiary = BeneficiarySerializer(read_only=True)

    class Meta:
        model = Contract
        fields = ['id', 'purchase', 'beneficiary', 'sum', 'security_amount', 'term', 'availability_payment',
                  'availability_sum', 'availability_share', 'treasury_support', 'number', 'create_at', 'update_at']
