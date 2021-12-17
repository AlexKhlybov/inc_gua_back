from rest_framework.viewsets import ModelViewSet

from app.service import custom_exception_handler
from ..models import Principal
from ..serializers import PrincipalFinancialIndicatorsSerializer


class PrincipalFinancialIndicatorsViewSet(ModelViewSet):
    queryset = Principal.objects.filter(legal_entity__inn=None)
    serializer_class = PrincipalFinancialIndicatorsSerializer

    def get_queryset(self):
        if self.request.GET.get('inn', None):
            return Principal.objects.filter(legal_entity__inn=self.request.GET.get('inn', None))
        return Principal.objects.filter(legal_entity__inn=None)

    def get_exception_handler(self):
        return custom_exception_handler
