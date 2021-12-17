from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
import django_filters
from django_filters.rest_framework import DjangoFilterBackend

from app.service import custom_exception_handler
from ..models import Limit
from ..serializers import LimitSerializer


class FilterSet(django_filters.FilterSet):
    principal = django_filters.Filter(field_name='principal')

    class Meta:
        model = Limit
        fields = ['principal']


class LimitViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet, UpdateModelMixin):
    queryset = Limit.objects.all()
    serializer_class = LimitSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FilterSet

    def list(self, request, *args, **kwargs):
        return super(LimitViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(LimitViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(LimitViewSet, self).update(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
