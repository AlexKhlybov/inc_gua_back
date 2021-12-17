from rest_framework import serializers
import logging
from ..models import Order
from entity.serializers.principal import PrincipalSerializer
from entity.serializers.beneficiary import BeneficiarySerializer
from bank.serializers.bank import BankSerializer
from user.serializers.user import UserSerializer
from .contest import ContestSerializer
from .order_special_condition import OrderSpecialConditionSerializer

logger = logging.getLogger(__name__)


class OrderListSerializer(serializers.ModelSerializer):
    principal = PrincipalSerializer(read_only=True)
    beneficiary = BeneficiarySerializer(read_only=True)
    contest = ContestSerializer(read_only=True)
    bank = BankSerializer(read_only=True)
    underwriter = UserSerializer(read_only=True)
    special_condition = OrderSpecialConditionSerializer(read_only=True, many=True)
    stop_factors = serializers.SerializerMethodField(read_only=True)
    pre_signals = serializers.SerializerMethodField(read_only=True)

    def get_stop_factors(self, obj):
        return obj.get_stop_factors()

    def get_pre_signals(self, obj):
        return obj.get_pre_signals()

    class Meta:
        model = Order
        fields = [
            'id', 'state', 'doc_type', 'principal', 'beneficiary', 'sum', 'guarantee_type', 'contest', 'bank',
            'underwriter', 'pnt', 'eis_link', 'start_date', 'end_date',
            'term', 'take_date', 'availability_without_acceptance', 'security_under_guarantee', 'provision',
            'provision_form', 'provision_sum', 'data_to_sign_txt_box', 'signature', 'signature_author',
            'report_pdf', 'pre_signals', 'stop_factors', 'is_quote_agreed', 'in_archive', 'uw_has_been_changed',
            'special_condition', 'create_at', 'update_at'
        ]


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'state', 'doc_type', 'principal', 'beneficiary', 'sum', 'guarantee_type', 'contest', 'bank',
            'underwriter', 'pnt', 'eis_link', 'start_date', 'end_date',
            'term', 'take_date', 'availability_without_acceptance', 'security_under_guarantee', 'provision',
            'provision_form', 'provision_sum', 'data_to_sign_txt_box', 'signature', 'signature_author',
            'report_pdf', 'is_quote_agreed', 'in_archive', 'uw_has_been_changed', 'special_condition', 'create_at', 'update_at'
        ]

    def update(self, instance, validated_data):
        try:
            if validated_data['state']:
                validated_data.pop('state')
        except Exception:
            print(Exception)
        return super().update(instance, validated_data)

    def create(self, validated_data):
        try:
            if validated_data['state']:
                validated_data.pop('state')
        except Exception:
            print(Exception)
        return super().create(validated_data)


class OrderUpdateStateSerializer(serializers.ModelSerializer):
    order = serializers.CharField()
    state = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Order
        fields = ['order', 'state', 'description']
