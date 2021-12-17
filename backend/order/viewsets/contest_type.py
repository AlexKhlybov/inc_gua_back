from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import ContestType
from ..serializers import ContestTypeSerializer


class ContestTypeViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = ContestType.objects.all()
    serializer_class = ContestTypeSerializer

    def list(self, request, *args, **kwargs):
        return super(ContestTypeViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(ContestTypeViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
