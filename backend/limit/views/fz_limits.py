import logging
from django.db.models import Sum
from django.db.models.functions import Coalesce

from ..models import FZLimits, LimitFZ
from order.models import Order

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class FZLimitsView(object):
    def __init__(self, init_params):
        self.fz_id = init_params['fz']
        self.fz = LimitFZ.objects.get(id=self.fz_id)

    def get_total_limit(self):
        item = LimitFZ.objects.filter(pk=self.fz.id)
        if not item:
            return 0
        result = LimitFZ.objects.get(pk=self.fz.id)
        if result:
            return result.limit
        return 0

    def get_current_guaranties_sum(self):
        guarantee_states = Order.get_guarantee_states()
        result = self.fz.fz_contest.all()
        result = Order.objects.filter(contest__in=result).filter(state__in=guarantee_states)
        result = result.annotate(current_sum=Coalesce(Sum('sum'), 0))
        if result:
            return result[0].current_sum
        return 0

    def get_orders_sum(self):
        order_states = Order.get_order_states()
        result = self.fz.fz_contest.all()
        result = Order.objects.filter(contest__in=result).filter(state__in=order_states)
        result = result.annotate(current_sum=Coalesce(Sum('sum'), 0))
        if result:
            return result[0].current_sum
        return 0

    def update(self):
        total_limit = self.get_total_limit()
        current_guaranties_sum = self.get_current_guaranties_sum()
        orders_sum = self.get_orders_sum()
        free_balance = total_limit - current_guaranties_sum - orders_sum
        item = FZLimits.objects.filter(fz=self.fz)
        if not item:
            fz_limit = FZLimits(fz=self.fz)
            fz_limit.save()
        fz_limit = FZLimits.objects.get(fz=self.fz)
        fz_limit.total_limit = total_limit
        fz_limit.current_guaranties_sum = current_guaranties_sum
        fz_limit.orders_sum = orders_sum
        fz_limit.free_balance = free_balance
        fz_limit.save()
        return fz_limit
