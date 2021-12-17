import django_filters
from rest_framework.viewsets import GenericViewSet
from rest_framework import filters, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from django_fsm_log.models import StateLog

from app.service import custom_exception_handler
from user.permissions import IsUnderwriterOrReject, IsMasterUnderwriterOrReject
from ..serializers import StateLogSerializer


class FilterSet(django_filters.FilterSet):
    source_state = django_filters.Filter(field_name='source_state')
    state = django_filters.Filter(field_name='state')
    transition = django_filters.Filter(field_name='transition')
    object_id = django_filters.Filter(field_name='object_id')

    class Meta:
        model = StateLog
        fields = ['source_state', 'state', 'transition', 'content_type', 'object_id', 'by']


class StateLogViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = StateLog.objects.all()
    serializer_class = StateLogSerializer
    permission_classes = [IsUnderwriterOrReject | IsMasterUnderwriterOrReject | permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FilterSet
    ordering_fields = ['id', 'timestamp', 'source_state', 'state', 'transition', 'content_type', 'object_id', 'by', 'description']

    def get_exception_handler(self):
        return custom_exception_handler
