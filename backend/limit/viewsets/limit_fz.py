from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import LimitFZ
from ..serializers import LimitFZSerializer


class LimitFZViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet, UpdateModelMixin):
    queryset = LimitFZ.objects.all()
    serializer_class = LimitFZSerializer

    def list(self, request, *args, **kwargs):
        return super(LimitFZViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(LimitFZViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
