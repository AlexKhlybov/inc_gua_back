import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import OliverWymanModel
from ..serializers import OlyverWymanAllSerializer


class FilterSet(django_filters.FilterSet):
    id = django_filters.Filter(field_name='id')
    supplier = django_filters.Filter(field_name='supplier')
    customer = django_filters.Filter(field_name='customer')
    purchaseNumber = django_filters.Filter(field_name='purchaseNumber')

    class Meta:
        model = OliverWymanModel
        fields = ['id', 'supplier', 'customer', 'purchaseNumber']


class OliverWymanViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = OliverWymanModel.objects.all()
    serializer_class = OlyverWymanAllSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FilterSet
    ordering_fields = ['id', 'supplier', 'customer', 'purchaseNumber']

    def get_queryset(self):
        if self.request.GET.get('purchaseNumber', None):
            return OliverWymanModel.objects.filter(purchaseNumber=self.request.GET.get('purchaseNumber', None))
        return OliverWymanModel.objects.filter(purchaseNumber=None)

    def list(self, request, *args, **kwargs):
        return super(OliverWymanViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(OliverWymanViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
