from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
import django_filters

from app.service import custom_exception_handler
from ..models import Factors
from ..serializers import FactorsSerializer, FactorsUpdateSerializer


class OrderFactorsFilterSet(django_filters.FilterSet):
    title = django_filters.Filter(field_name='title')
    catalog = django_filters.Filter(field_name='catalog')
    value = django_filters.Filter(field_name='value')

    class Meta:
        model = Factors
        fields = ['catalog']


class FactorsViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Factors.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = OrderFactorsFilterSet
    ordering_fields = ['title', 'catalog', 'value', ]

    def get_serializer_class(self):
        if self.action == 'update':
            return FactorsUpdateSerializer
        return FactorsSerializer

    def list(self, request, *args, **kwargs):
        return super(FactorsViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(FactorsViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(FactorsViewSet, self).update(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
