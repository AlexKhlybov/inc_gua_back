# import requests
import logging
# from rest_framework.response import Response
from django.db.models import Sum
from django.db.models.functions import Coalesce

from ..models import BankLimits, Bank
from limit.models import LimitBank
from order.models import Order

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class BankLimitsView(object):
    def __init__(self, init_params):
        self.bank_id = init_params['bank_id']
        self.bank = Bank.objects.get(id=self.bank_id)

    def get_total_limit(self):
        item = LimitBank.objects.filter(bank=self.bank)
        if not item:
            return 0
        result = LimitBank.objects.get(bank=self.bank)
        if result:
            return result.limit
        return 0

    def get_current_guaranties_sum(self):
        guarantee_states = Order.get_guarantee_states()
        result = self.bank.bank_order.filter(state__in=guarantee_states)
        result = result.annotate(current_sum=Coalesce(Sum('sum'), 0))
        if result:
            return result[0].current_sum
        return 0

    def get_orders_sum(self):
        order_states = Order.get_order_states()
        result = self.bank.bank_order.filter(state__in=order_states)
        result = result.annotate(current_sum=Coalesce(Sum('sum'), 0))
        if result:
            return result[0].current_sum
        return 0

    def update(self):
        total_limit = self.get_total_limit()
        current_guaranties_sum = self.get_current_guaranties_sum()
        orders_sum = self.get_orders_sum()
        free_balance = total_limit - current_guaranties_sum - orders_sum
        item = BankLimits.objects.filter(bank=self.bank)
        if not item:
            bank_limit = BankLimits(bank=self.bank)
            bank_limit.save()
        bank_limit = BankLimits.objects.get(bank=self.bank)
        bank_limit.total_limit = total_limit
        bank_limit.current_guaranties_sum = current_guaranties_sum
        bank_limit.orders_sum = orders_sum
        bank_limit.free_balance = free_balance
        bank_limit.save()
        return bank_limit
