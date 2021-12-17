from django.db import models

from app.mixins import Timestamps
from .order import Order


class OrderFactors(Timestamps):
    order = models.ForeignKey(Order, verbose_name='Заявка', on_delete=models.CASCADE, related_name='order_factors',
                              blank=False, null=False, default=None)
    factors = models.ForeignKey('Factors', verbose_name='Факторы', blank=True, null=True, default=None,
                                on_delete=models.SET_DEFAULT, related_name='factors')
    value = models.BooleanField(verbose_name='Значение', default=False)

    class Meta:
        verbose_name = 'Фактор заявки'
        verbose_name_plural = 'Факторы заявки'

    def __str__(self):
        return f"{self.order} - {self.factors} - {self.value}"
