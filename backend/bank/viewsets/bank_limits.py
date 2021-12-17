from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from app.service import custom_exception_handler
from ..models import BankLimits, Bank
from ..serializers import BankLimitsSerializer, BankLimitsUpdateSerializer
from ..views import BankLimitsView


class BankLimitsViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = BankLimits.objects.all()
    serializer_class = BankLimitsSerializer

    def get_serializer_class(self):
        if self.action == 'update_bank_limits':
            return BankLimitsUpdateSerializer
        return BankLimitsSerializer

    def list(self, request, *args, **kwargs):
        return super(BankLimitsViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(BankLimitsViewSet, self).retrieve(request, *args, **kwargs)

    @action(methods=['post'], detail=False)
    def update_bank_limits(self, request):
        data = request.data
        bank_id = data.get('bank', None)

        if not bank_id:
            return Response({'error': 'no bank'}, status=400)

        bank = Bank.objects.filter(id=bank_id)
        if not bank:
            return Response({'error': 'there is no bank with this id'}, status=400)
        init_params = {}
        init_params['bank_id'] = bank_id
        bank_limits = BankLimitsView(init_params=init_params)
        bank_limit = bank_limits.update()
        return Response({"status": True, "data": BankLimitsSerializer(bank_limit).data})

    def get_exception_handler(self):
        return custom_exception_handler
