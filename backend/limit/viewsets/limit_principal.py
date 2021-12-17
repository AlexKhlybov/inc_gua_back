import logging
import os
from decimal import Decimal

from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.utils.translation import gettext as _
import django_filters
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from app.service import custom_exception_handler
from entity.models.principal import Principal
from limit.models import Limit, LimitPrincipalModel
from order.models.order import Order
from ..serializers import LimitPrincipalSerializer, LimitPrincipalBaseSerializer, LimitPrincipalUpdateSerializer
from ..views import LimitPrincipal, PrincipalLimitsView

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class FilterSet(django_filters.FilterSet):
    principal = django_filters.Filter(field_name='principal')

    class Meta:
        model = LimitPrincipalModel
        fields = ['principal']


class LimitPrincipalViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet, UpdateModelMixin):
    queryset = LimitPrincipalModel.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FilterSet
    ordering_fields = ['id', 'principal']

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return LimitPrincipalBaseSerializer
        if self.action == 'update':
            return LimitPrincipalBaseSerializer
        if self.action == 'update_principal_limits':
            return LimitPrincipalUpdateSerializer
        if self.action == 'limit_principal_calculate':
            return LimitPrincipalSerializer
        return LimitPrincipalBaseSerializer

    def list(self, request, *args, **kwargs):
        return super(LimitPrincipalViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(LimitPrincipalViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(LimitPrincipalViewSet, self).update(request, *args, **kwargs)

    @action(methods=["post"], detail=False)
    def limit_principal_calculate(self, request):
        if (not os.getenv("KONTUR_KEY") or not
                os.getenv("KONTUR_URL_GOV_PURCHASES") or not
                os.getenv("KONTUR_URL_BUH") or not
                os.getenv("KONTUR_URL_DETAIL")):
            return Response({"error": _("there is no kontur_key or kontur_url in environment")}, status=400)
        data = request.data
        inn = data.get("inn", None)
        if not inn:
            return Response({"error": "no inn"}, status=400)
        try:
            principal = Principal.objects.get(legal_entity__inn=inn)
            order = Order.objects.filter(principal=principal.id)[0]

        except Exception as e:
            logging.error(e)
            return Response({"error": _("principal or order not exist")}, status=400)
        try:
            calculate_lp = LimitPrincipal(inn, order.sum)
        except Exception as e:
            logging.error(e)
            return Response({"error": _("there is no amount in the application")}, status=400)
        try:
            lp = calculate_lp.get_limit_principal()
            item = LimitPrincipalModel.objects.filter(principal=principal)
            if not item:
                limit_principal = LimitPrincipalModel(principal=principal)
                limit_principal.save()
            limit_principal = LimitPrincipalModel.objects.get(principal=principal)
            limit_principal.limit = Decimal(lp["limit"])
            limit_principal.save()
            # не работает, пришлось переписать выше
            # limit_principal, created = Limit.objects.update_or_create(
            #     principal=principal,
            #     defaults={
            #         "limit": lp["limit"],
            #     },
            # )
            # print(f'ball_rating = {Decimal(lp["ball_rating"])}, type = {type(Decimal(lp["ball_rating"]))}')
            obj, created = Limit.objects.update_or_create(
                principal=principal,
                defaults={
                    "limit_principal": limit_principal,
                    "ball_rating": Decimal(lp["ball_rating"]),
                    "letter_rating": lp["letter_rating"],
                    "financial_indicators": lp["financial_indicators"],
                    "score_big_contracts": lp["score_big_contracts"],
                    "score_all_contracts": lp["score_all_contracts"],
                    "score_year": lp["score_year"],
                    "work_exp": lp["work_exp"],
                    "additional_factors": Decimal(lp["additional_factors"]),
                    "add_factor_1": Decimal(-0.11 if lp["factors"]['factor_1'] else 0),
                    "add_factor_2": -0.11 if lp["factors"]['factor_2'] else 0,
                    "add_factor_3": -0.11 if lp["factors"]['factor_3'] else 0,
                    "add_factor_4": -0.11 if lp["factors"]['factor_4'] else 0,
                    "add_factor_5": -0.11 if lp["factors"]['factor_5'] else 0,
                    "add_factor_6": -0.11 if lp["factors"]['factor_6'] else 0,
                    "add_factor_7": -0.11 if lp["factors"]['factor_7'] else 0,
                    "add_factor_8": -0.11 if lp["factors"]['factor_8'] else 0,
                    "add_factor_9": -0.11 if lp["factors"]['factor_9'] else 0,
                },
            )
            return Response({"status": True, "limit_principal": lp})
        except Exception as e:
            logging.error(e)
            return Response({"error": _("no data on the principal with the given inn")}, status=400)

    @action(methods=['post'], detail=False)
    def update_principal_limits(self, request):
        data = request.data
        principal_id = data.get('principal', None)

        if not principal_id:
            return Response({'error': 'no principal'}, status=400)

        principal = Principal.objects.filter(id=principal_id)
        if not principal:
            return Response({'error': 'there is no principal with this id'}, status=400)
        init_params = {}
        init_params['principal_id'] = principal_id
        principal_limits = PrincipalLimitsView(init_params=init_params)
        principal_limit = principal_limits.update()
        return Response({"status": True, "data": LimitPrincipalBaseSerializer(principal_limit).data})

    def get_exception_handler(self):
        return custom_exception_handler
