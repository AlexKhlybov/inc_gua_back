import os

import django_filters
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import filters, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from django.utils.translation import gettext as _

from app.service import custom_exception_handler
from ..models import Order
from ..serializers import OrderListSerializer, KonturPrincipalSerializer, OlyverWymanSerializer,\
    GetFactorsSerializer, OrderUpdateSerializer, OrderUpdateStateSerializer
from ..views import Kontur, OliverWyman, GetFactors
from entity.models.principal import Principal
from entity.models.beneficiary import Beneficiary
from user.permissions import IsUnderwriterOrReject, IsMasterUnderwriterOrReject


class OrderFilterSet(django_filters.FilterSet):
    id = django_filters.Filter(field_name='id')
    principal = django_filters.Filter(field_name='principal')
    underwriter = django_filters.Filter(field_name='underwriter')
    doc_type = django_filters.Filter(field_name='doc_type')
    state = django_filters.Filter(field_name='state')
    sum = django_filters.Filter(method='sum_function')
    contest__type = django_filters.Filter(field_name='contest__type')
    contest__fz__fz = django_filters.Filter(field_name='contest__fz__fz')
    year = django_filters.Filter(method='year_function')

    def sum_function(self, request, name, value):
        if value:
            value = [int(item) for item in value.split(',')]
            qs = request.filter(sum__gte=min(value),
                                sum__lte=max(value))
            return qs
        return request

    def year_function(self, request, name, value):
        if value:
            value = [int(item) for item in value.split(',')]
            qs = request.filter(start_date__year__gte=min(value),
                                start_date__year__lte=max(value))
            return qs
        return request

    class Meta:
        model = Order
        fields = ['id', 'principal', 'state', 'contest__type', 'contest__fz__fz', 'sum', 'year', 'underwriter']


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = OrderFilterSet
    ordering_fields = ['id', 'principal', 'start_date', 'doc_type', 'sum', 'contest__type', 'contest__fz__fz', 'state', 'underwriter']
    permission_classes = [IsUnderwriterOrReject | IsMasterUnderwriterOrReject | permissions.IsAdminUser]
    permission_classes_by_action = {
        'list': [IsUnderwriterOrReject | IsMasterUnderwriterOrReject | permissions.IsAdminUser],
        'retrieve': [IsUnderwriterOrReject | IsMasterUnderwriterOrReject | permissions.IsAdminUser],
        'create': [IsUnderwriterOrReject | IsMasterUnderwriterOrReject | permissions.IsAdminUser],
        'update': [IsUnderwriterOrReject | IsMasterUnderwriterOrReject | permissions.IsAdminUser],
        'destroy': [IsUnderwriterOrReject | IsMasterUnderwriterOrReject | permissions.IsAdminUser],
        'partial_update': [IsUnderwriterOrReject | IsMasterUnderwriterOrReject | permissions.IsAdminUser],
        'partial_destroy': [IsUnderwriterOrReject | IsMasterUnderwriterOrReject | permissions.IsAdminUser],
        'kontur_financial_indicators': [IsUnderwriterOrReject | IsMasterUnderwriterOrReject | permissions.IsAdminUser],
        'olyver_wyman_score_guarantee': [IsUnderwriterOrReject | IsMasterUnderwriterOrReject | permissions.IsAdminUser],
        'update_state': [permissions.IsAdminUser],
        'to_underwriting_a_new_application': [IsMasterUnderwriterOrReject | permissions.IsAdminUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'kontur_financial_indicators':
            return KonturPrincipalSerializer
        if self.action == 'olyver_wyman_score_guarantee':
            return OlyverWymanSerializer
        if self.action == 'get_factors':
            return GetFactorsSerializer
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return OrderUpdateSerializer
        if self.action == 'list' or self.action == 'retrieve':
            return OrderListSerializer
        if self.action == 'update_state':
            return OrderUpdateStateSerializer
        return GetFactorsSerializer

    def list(self, request, *args, **kwargs):
        return super(OrderViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(OrderViewSet, self).retrieve(request, *args, **kwargs)

    def return_order_from_req(self, request):
        data = request.data
        order_id = data.get('order', None)
        description = data.get('description', None)

        if not order_id:
            return Response({'error': _('no order')}, status=400)

        order = Order.objects.filter(pk=order_id)
        if not order:
            return Response({'error': _('there is no order with this id')}, status=400)
        description = description if description else ''
        instance = order[0]
        out_data = {'instance': instance, 'description': description}
        return out_data

    def exec_method(self, request, func):
        data = self.return_order_from_req(request)
        if isinstance(data, Response):
            return data
        instance = data['instance']
        description = data['description']
        if not description:
            description = func
        getattr(instance, func)(by=request.user, description=description)
        instance.save()
        return Response({"status": True, "data": OrderListSerializer(instance).data})

    @action(methods=['post'], detail=False)
    def update_state(self, request):
        state = request.data.get('state', None)
        data = self.return_order_from_req(request)
        if isinstance(data, Response):
            return data
        if state:
            instance = data['instance']
            description = data['description']
            instance.update_state(state=state, by=request.user, description=description)
            instance.save()
            return Response({"status": True, "data": OrderListSerializer(instance).data})
        return Response({"status": True, "data": 'Данные не были изменены'})

    @action(methods=['post'], detail=False)
    def to_state_underwriting_a_new_application(self, request):
        return self.exec_method(request, 'to_state_underwriting_a_new_application')

    @action(methods=['post'], detail=False)
    def to_state_underwriting_in_progress(self, request):
        return self.exec_method(request, 'to_state_underwriting_in_progress')

    @action(methods=['post'], detail=False)
    def to_state_underwriting_requery(self, request):
        return self.exec_method(request, 'to_state_underwriting_requery')

    @action(methods=['post'], detail=False)
    def to_state_quote_auto(self, request):
        return self.exec_method(request, 'to_state_quote_auto')

    @action(methods=['post'], detail=False)
    def to_state_quote_auction(self, request):
        return self.exec_method(request, 'to_state_quote_auction')

    @action(methods=['post'], detail=False)
    def to_state_quote_individual(self, request):
        return self.exec_method(request, 'to_state_quote_individual')

    @action(methods=['post'], detail=False)
    def to_state_underwriting_refusal(self, request):
        return self.exec_method(request, 'to_state_underwriting_refusal')

    @action(methods=['post'], detail=False)
    def to_state_quote_sent(self, request):
        return self.exec_method(request, 'to_state_quote_sent')

    @action(methods=['post'], detail=False)
    def to_state_in_archive(self, request):
        return self.exec_method(request, 'to_state_in_archive')

    @action(methods=['post'], detail=False)
    def to_state_quote_redefined(self, request):
        return self.exec_method(request, 'to_state_quote_redefined')

    @action(methods=['post'], detail=False)
    def to_state_quote_refusal(self, request):
        return self.exec_method(request, 'to_state_quote_refusal')

    @action(methods=['post'], detail=False)
    def to_state_quote_agreed(self, request):
        return self.exec_method(request, 'to_state_quote_agreed')

    @action(methods=['post'], detail=False)
    def to_state_documents_requery(self, request):
        return self.exec_method(request, 'to_state_documents_requery')

    @action(methods=['post'], detail=False)
    def to_state_documents_signature(self, request):
        return self.exec_method(request, 'to_state_documents_signature')

    @action(methods=['post'], detail=False)
    def to_state_documents_refusal(self, request):
        return self.exec_method(request, 'to_state_documents_refusal')

    @action(methods=['post'], detail=False)
    def to_state_guarantee_issue_requested(self, request):
        return self.exec_method(request, 'to_state_guarantee_issue_requested')

    @action(methods=['post'], detail=False)
    def to_state_guarantee_issued_payment_expected(self, request):
        return self.exec_method(request, 'to_state_guarantee_issued_payment_expected')

    @action(methods=['post'], detail=False)
    def to_state_guarantee_disclaimer(self, request):
        return self.exec_method(request, 'to_state_guarantee_disclaimer')

    @action(methods=['post'], detail=False)
    def to_state_guarantee_valid(self, request):
        return self.exec_method(request, 'to_state_guarantee_valid')

    @action(methods=['post'], detail=False)
    def kontur_financial_indicators(self, request):
        if not os.getenv('KONTUR_KEY') or not os.getenv('KONTUR_URL'):
            return Response({'error': _('there is no kontur_key or kontur_url in environment')}, status=400)
        kontur = Kontur()
        data = request.data
        inn = data.get('inn', None)
        if not inn:
            return Response({'error': 'no inn'}, status=400)
        principal = Principal.objects.filter(legal_entity__inn=inn)
        if not principal:
            return Response({'error': _('there is no principal with this inn')}, status=400)
        kontur.get_kontur_financial_indicators(inn)
        return Response({"status": True})

    @action(methods=['post'], detail=False)
    def olyver_wyman_score_guarantee(self, request):
        if not os.getenv('OW_URL') or not os.getenv('OW_LOGIN') or not os.getenv('OW_PASSWORD'):
            return Response({'error': _('there are no oliver_wyman params in environment')}, status=400)
        data = request.data
        supplierInn = data.get('supplierInn', None)
        customerInn = data.get('customerInn', None)
        purchaseNumber = data.get('purchaseNumber', None)

        if not supplierInn:
            return Response({'error': _('no supplierInn')}, status=400)
        if not customerInn:
            return Response({'error': _('no customerInn')}, status=400)

        principal = Principal.objects.filter(legal_entity__inn=supplierInn)
        beneficiary = Beneficiary.objects.filter(legal_entity__inn=customerInn)
        if not principal:
            return Response({'error': _('there is no principal with this supplierInn')}, status=400)
        if not beneficiary:
            return Response({'error': _('there is no beneficiary with this customerInn')}, status=400)
        if principal.count() > 1:
            return Response({'error': _('there are more then one principal with this supplierInn')}, status=400)
        if beneficiary.count() > 1:
            return Response({'error': _('there are more then one beneficiary with this customerInn')}, status=400)
        init_params = {'supplierInn': supplierInn, 'customerInn': customerInn}
        if purchaseNumber:
            init_params['purchaseNumber'] = purchaseNumber
        olyver_wyman = OliverWyman(init_params=init_params)
        output_data = olyver_wyman.get_olyver_wyman_score_guarantee()
        return Response({"status_code": 201, "data": output_data})

    @action(methods=['post'], detail=False)
    def get_factors(self, request):
        data = request.data
        order_id = data.get('order', None)

        if not order_id:
            return Response({'error': _('no order')}, status=400)

        order = Order.objects.filter(pk=order_id)
        if not order:
            return Response({'error': _('there is no order with this id')}, status=400)

        init_params = {'order': order_id}
        factors = GetFactors(init_params=init_params)
        output_data = factors.update_base()
        return Response({"status_code": 201, "data": output_data})

    @action(methods=['get'], detail=False)
    def get_all_states(self, request):
        return Response({"states": Order.get_all_states()})

    @action(methods=['get'], detail=False)
    def get_order_states(self, request):
        states = Order.get_order_states()
        states.append('UNDERWRITING_REFUSAL')
        states.append('QUOTE_REFUSAL')
        states.append('DOCUMENTS_REFUSAL')
        states.append('IN_ARCHIVE')
        return Response({"states": states})

    @action(methods=['get'], detail=False)
    def get_guarantee_states(self, request):
        states = Order.get_guarantee_states()
        states.append('GUARANTEE_DISCLAIMER')
        states.append('GUARANTEE_EXPIRED')
        states.append('GUARANTEE_TERMINATED')
        states.append('IN_ARCHIVE')
        return Response({"states": states})

    def get_exception_handler(self):
        return custom_exception_handler
