from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import Purchase
from ..serializers import PurchaseSerializer


class PurchaseViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def list(self, request, *args, **kwargs):
        return super(PurchaseViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PurchaseViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
