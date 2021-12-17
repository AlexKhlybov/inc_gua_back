from decimal import Decimal
from django.db import models

from app.mixins import Timestamps


class LimitFZ(Timestamps):
    fz = models.CharField(max_length=32, verbose_name='ФЗ', blank=False, null=False, default=None)
    limit = models.DecimalField(verbose_name='Лимит', max_digits=32, decimal_places=2, default=Decimal('0.00'))

    class Meta:
        verbose_name = 'ФЗ'
        verbose_name_plural = 'ФЗ'

    def __str__(self):
        return f'ФЗ - {self.fz}'
