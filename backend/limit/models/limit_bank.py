from decimal import Decimal
from django.db import models

from app.mixins import Timestamps
from bank.models import Bank


class LimitBank(Timestamps):
    bank = models.OneToOneField(Bank, on_delete=models.CASCADE, related_name='limit_bank', blank=False, null=False,
                                verbose_name='Банк', default=None)
    limit = models.DecimalField(verbose_name='Лимит', max_digits=32, decimal_places=2, default=Decimal('0.00'))

    class Meta:
        verbose_name = 'Установленный лимит банка'
        verbose_name_plural = 'Установленные лимиты банков'

    def __str__(self):
        return f'{self.bank} - {self.limit}'
