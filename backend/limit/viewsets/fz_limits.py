from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from app.service import custom_exception_handler
from ..models import FZLimits, LimitFZ
from ..serializers import FZLimitsSerializer, FZLimitsUpdateSerializer
from ..views import FZLimitsView


class FZLimitsViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = FZLimits.objects.all()
    serializer_class = FZLimitsSerializer

    def get_serializer_class(self):
        if self.action == 'update_fz_limits':
            return FZLimitsUpdateSerializer
        return FZLimitsSerializer

    def list(self, request, *args, **kwargs):
        return super(FZLimitsViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(FZLimitsViewSet, self).retrieve(request, *args, **kwargs)

    @action(methods=['post'], detail=False)
    def update_fz_limits(self, request):
        data = request.data
        fz_id = data.get('fz', None)

        if not fz_id:
            return Response({'error': 'no fz'}, status=400)

        fz = LimitFZ.objects.filter(id=fz_id)
        if not fz:
            return Response({'error': 'there is no fz with this id'}, status=400)
        init_params = {}
        init_params['fz'] = fz_id
        fz_limits = FZLimitsView(init_params=init_params)
        fz_limit = fz_limits.update()
        return Response({"status": True, "data": FZLimitsSerializer(fz_limit).data})

    def get_exception_handler(self):
        return custom_exception_handler
