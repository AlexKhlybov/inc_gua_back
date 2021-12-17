from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status

from app.service import custom_exception_handler
from ..models import OrderDocument
from ..serializers import OrderDocumentSerializer, OrderDocumentCreateSerializer, OrderDocumentUpdateSerializer
from app.utils import MultipartJSONParser


class FilterSet(django_filters.FilterSet):
    order = django_filters.Filter(field_name='order')
    document_type = django_filters.Filter(field_name='document_type')
    document_type__type = django_filters.Filter(field_name='document_type__type')
    is_valid = django_filters.Filter(field_name='is_valid')

    class Meta:
        model = OrderDocument
        fields = ['order', 'document_type', 'is_valid']


class OrderDocumentViewSet(ModelViewSet):
    queryset = OrderDocument.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FilterSet
    ordering_fields = ['id', 'order', 'document_type', 'document_type__type', 'is_valid', 'update_at']

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderDocumentCreateSerializer
        if self.action == 'update':
            return OrderDocumentUpdateSerializer
        return OrderDocumentSerializer

    def list(self, request, *args, **kwargs):
        return super(OrderDocumentViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(OrderDocumentViewSet, self).retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(OrderDocumentViewSet, self).destroy(request, *args, **kwargs)

    @action(methods=['post'], parser_classes=(MultipartJSONParser,), detail=False)
    def upload_file(self, request, *args, **kwargs):
        serializer = OrderDocumentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        result = Response(serializer.data, status=status.HTTP_201_CREATED)
        return result

    def get_exception_handler(self):
        return custom_exception_handler
