from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from app.service import custom_exception_handler
from ..models import BankDocument
from ..serializers import BankDocumentSerializer


class FilterSet(django_filters.FilterSet):
    bank = django_filters.Filter(field_name='bank')
    document_type = django_filters.Filter(field_name='document_type')

    class Meta:
        model = BankDocument
        fields = ['bank', 'document_type']


class BankDocumentViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = BankDocument.objects.all()
    serializer_class = BankDocumentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FilterSet
    ordering_fields = ['id', 'bank', 'document_type']

    def list(self, request, *args, **kwargs):
        return super(BankDocumentViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(BankDocumentViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
