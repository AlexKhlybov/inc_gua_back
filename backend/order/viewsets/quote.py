from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.translation import gettext as _

from app.service import custom_exception_handler
from ..models.quote import Quote
from ..serializers.quote import QuoteSerializer, QuoteCreateSerializer, GetSumSerializer


class QuoteViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Quote.objects.all()

    def get_serializer_class(self):
        if self.action == 'get_sum':
            return GetSumSerializer
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return QuoteCreateSerializer
        return QuoteSerializer

    def list(self, request, *args, **kwargs):
        return super(QuoteViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(QuoteViewSet, self).retrieve(request, *args, **kwargs)

    @action(methods=['post'], detail=False)
    def get_sum(self, request):
        data = request.data
        sum = data.get('sum', None)
        rate = data.get('rate', None)

        if not sum:
            return Response({'error': _('no sum')}, status=400)
        if not rate:
            return Response({'error': _('no rate')}, status=400)

        output_data = int(sum) * int(rate) / 100
        return Response({"status_code": 201, "data": output_data})

    def get_exception_handler(self):
        return custom_exception_handler
