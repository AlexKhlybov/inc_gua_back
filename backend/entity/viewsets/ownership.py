from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models.ownership import Ownership
from ..serializers.ownership import OwnershipSerializer


class OwnershipViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Ownership.objects.all()
    serializer_class = OwnershipSerializer

    def list(self, request, *args, **kwargs):
        return super(OwnershipViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(OwnershipViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
