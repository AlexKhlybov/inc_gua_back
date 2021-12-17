from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import Lot
from ..serializers import LotSerializer


class LotViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer

    def list(self, request, *args, **kwargs):
        return super(LotViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(LotViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
