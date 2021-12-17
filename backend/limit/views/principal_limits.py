import logging
from django.db.models import Sum
from django.db.models.functions import Coalesce

from ..models import LimitPrincipalModel
from entity.models.principal import Principal
from order.models import Order

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class PrincipalLimitsView(object):
    def __init__(self, init_params):
        self.principal_id = init_params['principal_id']
        self.principal = Principal.objects.get(id=self.principal_id)

    def get_total_limit(self):
        item = LimitPrincipalModel.objects.filter(principal=self.principal)
        if not item:
            return 0
        result = LimitPrincipalModel.objects.get(principal=self.principal)
        if result:
            return result.limit
        return 0

    def get_current_guaranties_sum(self):
        guarantee_states = Order.get_guarantee_states()
        result = self.principal.principal_orders.filter(state__in=guarantee_states)
        result = result.annotate(current_sum=Coalesce(Sum('sum'), 0))
        if result:
            return result[0].current_sum
        return 0

    def get_orders_sum(self):
        order_states = Order.get_order_states()
        result = self.principal.principal_orders.filter(state__in=order_states)
        result = result.annotate(current_sum=Coalesce(Sum('sum'), 0))
        if result:
            return result[0].current_sum
        return 0

    def update(self):
        limit = self.get_total_limit()
        current_guaranties_sum = self.get_current_guaranties_sum()
        orders_sum = self.get_orders_sum()

        item = LimitPrincipalModel.objects.filter(principal=self.principal)
        if not item:
            principal_limit = LimitPrincipalModel(principal=self.principal)
            principal_limit.save()
        principal_limit = LimitPrincipalModel.objects.get(principal=self.principal)
        principal_limit.limit = limit
        principal_limit.current_guaranties_sum = current_guaranties_sum
        principal_limit.orders_sum = orders_sum
        principal_limit.total_limit = limit if principal_limit.total_limit == 0 else principal_limit.total_limit
        free_balance = principal_limit.total_limit - current_guaranties_sum - orders_sum
        principal_limit.free_balance = free_balance
        principal_limit.save()
        return principal_limit
