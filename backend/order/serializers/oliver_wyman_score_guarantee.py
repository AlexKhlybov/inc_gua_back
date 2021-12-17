from rest_framework import serializers

from ..models import OliverWymanModel
from entity.serializers.principal import PrincipalSerializer
from entity.serializers.beneficiary import BeneficiarySerializer


class OlyverWymanSerializer(serializers.ModelSerializer):
    class Meta:
        model = OliverWymanModel
        fields = ['supplierInn', 'customerInn', 'purchaseNumber', 'create_at', 'update_at']


class OlyverWymanAllSerializer(serializers.ModelSerializer):
    supplier = PrincipalSerializer(read_only=True)
    customer = BeneficiarySerializer(read_only=True)

    class Meta:
        model = OliverWymanModel
        fields = '__all__'
