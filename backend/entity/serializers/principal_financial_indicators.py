from rest_framework import serializers

from ..models import Principal


class PrincipalFinancialIndicatorsSerializer(serializers.ModelSerializer):
    financial_indicators = serializers.SerializerMethodField()

    def get_financial_indicators(self, obj):
        return obj.get_financial_indicators()

    class Meta:
        model = Principal
        fields = ['id', 'title', 'legal_entity', 'financial_indicators', 'create_at', 'update_at']
