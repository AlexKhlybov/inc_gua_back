from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
import django_filters
from rest_framework.viewsets import GenericViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

from app.service import custom_exception_handler
from user.permissions import IsUnderwriterOrReject, IsMasterUnderwriterOrReject
from ..serializers import OrderQuoteSerializer
from ..models import OrderQuote


class FilterSet(django_filters.FilterSet):
    order = django_filters.Filter(field_name='order')
    quote = django_filters.Filter(field_name='quote')

    class Meta:
        model = OrderQuote
        fields = ['order', 'quote']


class OrderQuoteViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = OrderQuote.objects.all()
    serializer_class = OrderQuoteSerializer
    permission_classes = [IsUnderwriterOrReject | IsMasterUnderwriterOrReject | permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FilterSet
    ordering_fields = ['id', 'order', 'quote']

    def list(self, request, *args, **kwargs):
        return super(OrderQuoteViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(OrderQuoteViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
