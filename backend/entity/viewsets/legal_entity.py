from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import LegalEntity
from ..serializers import LegalEntitySerializer


class LegalEntityViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer

    def list(self, request, *args, **kwargs):
        return super(LegalEntityViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(LegalEntityViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
