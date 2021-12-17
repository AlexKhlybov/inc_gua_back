from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import Bank
from ..serializers import BankSerializer


class BankViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    def list(self, request, *args, **kwargs):
        return super(BankViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(BankViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
