from rest_framework import serializers

from ..models import Principal
from .legal_entity import LegalEntitySerializer


class PrincipalSerializer(serializers.ModelSerializer):
    legal_entity = LegalEntitySerializer(read_only=True)

    class Meta:
        model = Principal
        fields = '__all__'
