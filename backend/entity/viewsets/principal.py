from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
import django_filters
from django_filters.rest_framework import DjangoFilterBackend

from app.service import custom_exception_handler
from ..models import Principal
from ..serializers import PrincipalSerializer


class FilterSet(django_filters.FilterSet):
    legal_entity__inn = django_filters.Filter(field_name='legal_entity__inn')
    title = django_filters.Filter(field_name='title')

    class Meta:
        model = Principal
        fields = ['legal_entity__inn', 'title']


class PrincipalViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Principal.objects.all()
    serializer_class = PrincipalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FilterSet

    def list(self, request, *args, **kwargs):
        return super(PrincipalViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PrincipalViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
