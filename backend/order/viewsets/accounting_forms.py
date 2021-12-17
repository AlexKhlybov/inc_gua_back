from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from app.service import custom_exception_handler
from ..models import AccountingForm
from ..serializers import AccountingFormSerializer


class FilterSet(django_filters.FilterSet):
    id = django_filters.Filter(field_name='id')
    principal = django_filters.Filter(field_name='principal')
    year = django_filters.Filter(field_name='year')

    class Meta:
        model = AccountingForm
        fields = ['id', 'principal', 'year']


class AccountingFormViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = AccountingForm.objects.all()
    serializer_class = AccountingFormSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FilterSet
    ordering_fields = ['id', 'principal', 'year']

    def list(self, request, *args, **kwargs):
        return super(AccountingFormViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(AccountingFormViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
