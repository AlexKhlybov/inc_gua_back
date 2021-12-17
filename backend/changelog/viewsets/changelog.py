
import django_filters

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework import filters

from app.service import custom_exception_handler
from ..models import ChangeLog
from ..serializers import ChangeLogSerializer


class ChangeLogFilterSet(django_filters.FilterSet):
    id = django_filters.Filter(field_name='id')
    changed = django_filters.Filter(field_name='changed')
    user = django_filters.Filter(field_name='user')
    role = django_filters.Filter(field_name='role')
    action_on_model = django_filters.Filter(field_name='action_on_model')
    name = django_filters.Filter(field_name='name')
    content_type = django_filters.Filter(field_name='content_type')
    content_type__model = django_filters.Filter(field_name='content_type__model')
    object_id = django_filters.Filter(field_name='object_id')

    class Meta:
        model = ChangeLog
        fields = ['id', 'changed', 'user', 'role', 'action_on_model', 'name', 'content_type', 'content_type__model', 'object_id']


class ChangeLogViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = ChangeLog.objects.all()
    serializer_class = ChangeLogSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ChangeLogFilterSet
    ordering_fields = ['id', 'changed', 'user', 'role', 'action_on_model', 'name', 'content_type', 'object_id']

    def list(self, request, *args, **kwargs):
        return super(ChangeLogViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(ChangeLogViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler
