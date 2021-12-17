from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import Beneficiary
from ..serializers import BeneficiarySerializer


class BeneficiaryViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer

    def list(self, request, *args, **kwargs):
        return super(BeneficiaryViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(BeneficiaryViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
