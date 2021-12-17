from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from app.service import custom_exception_handler
from ..models.document_type import DocumentType
from ..serializers.document_type import DocumentTypeSerializer


class FilterSet(django_filters.FilterSet):
    type = django_filters.Filter(field_name='type')
    title = django_filters.Filter(field_name='title')

    class Meta:
        model = DocumentType
        fields = ['type', 'title']


class DocumentTypeViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet, CreateModelMixin):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FilterSet
    ordering_fields = ['id', 'type', 'title']

    def list(self, request, *args, **kwargs):
        return super(DocumentTypeViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(DocumentTypeViewSet, self).retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(DocumentTypeViewSet, self).create(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
