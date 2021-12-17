from rest_framework import serializers

from ..models import AccountingForm, AccountingFormDetail
from entity.serializers.principal import PrincipalSerializer


class AccountingFormDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingFormDetail
        fields = '__all__'


class AccountingFormSerializer(serializers.ModelSerializer):
    principal = PrincipalSerializer(read_only=True)
    detail_form = AccountingFormDetailSerializer(many=True, read_only=True)

    class Meta:
        model = AccountingForm
        fields = [
            'id', 'principal', 'year', 'detail_form'
        ]
