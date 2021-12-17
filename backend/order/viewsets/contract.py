from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import Contract
from ..serializers import ContractSerializer


class ContractViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet, UpdateModelMixin):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def list(self, request, *args, **kwargs):
        return super(ContractViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(ContractViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
