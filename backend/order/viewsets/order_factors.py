import django_filters
from rest_framework import filters
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from app.service import custom_exception_handler
from ..models import OrderFactors
from ..serializers import OrderFactorsSerializer


class ResultPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 1000


class OrderFactorsFilterSet(django_filters.FilterSet):
    order = django_filters.Filter(field_name='order')
    factors__catalog = django_filters.Filter(field_name='factors__catalog')
    value = django_filters.Filter(field_name='value')

    class Meta:
        model = OrderFactors
        fields = ['order', 'factors__catalog', 'value']


class OrderFactorsViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = OrderFactors.objects.filter(factors__value=True).order_by('-value')
    pagination_class = ResultPagination
    serializer_class = OrderFactorsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = OrderFactorsFilterSet
    ordering_fields = ['order', 'factors__catalog', 'value']

    def list(self, request, *args, **kwargs):
        return super(OrderFactorsViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(OrderFactorsViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
