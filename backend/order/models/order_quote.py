from django.db import models

from app.mixins import Timestamps
from .order import Order
from .quote import Quote


class OrderQuote(Timestamps):
    order = models.ForeignKey(Order, verbose_name='Заявка', on_delete=models.CASCADE, related_name='order_quotes',
                              blank=False, null=False, default=None)
    quote = models.ForeignKey(Quote, verbose_name='Котировка', blank=True, null=True, default=None,
                              on_delete=models.SET_DEFAULT, related_name='quotes')

    class Meta:
        verbose_name = 'Котировка заявки'
        verbose_name_plural = 'Котировки заявки'

    def __str__(self):
        return f"{self.order} - {self.quote}"
