from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import LimitBank
from ..serializers import LimitBankSerializer


class LimitBankViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet, UpdateModelMixin):
    queryset = LimitBank.objects.all()
    serializer_class = LimitBankSerializer

    def list(self, request, *args, **kwargs):
        return super(LimitBankViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(LimitBankViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
