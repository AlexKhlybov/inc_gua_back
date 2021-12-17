from rest_framework import serializers

from ..models import Beneficiary
from .legal_entity import LegalEntitySerializer


class BeneficiarySerializer(serializers.ModelSerializer):
    legal_entity = LegalEntitySerializer(read_only=True)

    class Meta:
        model = Beneficiary
        fields = '__all__'
