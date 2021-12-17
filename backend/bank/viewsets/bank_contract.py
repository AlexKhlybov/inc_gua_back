from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import BankСontract
from ..serializers import BankСontractSerializer


class BankСontractViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = BankСontract.objects.all()
    serializer_class = BankСontractSerializer

    def list(self, request, *args, **kwargs):
        return super(BankСontractViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(BankСontractViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
