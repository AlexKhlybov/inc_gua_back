from rest_framework import serializers
from ..models.quote import Quote
from ..serializers.auction import AuctionSerializer
from bank.serializers.bank import BankSerializer


class QuoteSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    auction = AuctionSerializer(read_only=True)
    bank = BankSerializer(read_only=True)

    def get_type(self, obj):
        return obj.get_type_display()

    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Quote
        fields = (
            'id', 'auction', 'bank', 'guarantee_rate', 'guarantee_sum', 'total_commission',
            'bank_rate', 'bank_sum', 'bank_commission',
            'insurance_premium_rate', 'insurance_premium_sum', 'insurance_premium_commission', 'master_agent_rate',
            'master_agent_sum', 'master_agent_commission', 'agent_rate', 'agent_sum', 'agent_commission', 'type',
            'status', 'expiry_date', 'is_edited'
        )


class QuoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = [
            'id', 'auction', 'bank', 'guarantee_rate', 'guarantee_sum', 'total_commission', 'bank_rate', 'bank_sum',
            'insurance_premium_rate', 'insurance_premium_sum', 'master_agent_rate',
            'master_agent_sum', 'agent_rate', 'agent_sum', 'type',
            'status', 'expiry_date', 'is_edited'
        ]


class GetSumSerializer(serializers.Serializer):
    sum = serializers.IntegerField()
    rate = serializers.IntegerField()
