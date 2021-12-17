from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import models

from app.mixins import Timestamps
from .bank import Bank


class BankLimits(Timestamps):

    bank = models.OneToOneField(Bank, verbose_name='Банк', related_name='bank_limits', blank=False, null=True,
                                on_delete=models.CASCADE)
    total_limit = models.DecimalField(verbose_name='Установленный лимит', max_digits=32, decimal_places=2,
                                      default=Decimal('0.00'))
    current_guaranties_sum = models.DecimalField(verbose_name='Действующие БГ', max_digits=32, decimal_places=2,
                                                 default=Decimal('0.00'))
    orders_sum = models.DecimalField(verbose_name='Общая сумма заявок', max_digits=32, decimal_places=2, default=Decimal('0.00'))
    free_balance = models.DecimalField(verbose_name='Свободный остаток', max_digits=32, decimal_places=2,
                                       default=Decimal('0.00'))

    class Meta:
        verbose_name = 'Лимит банка'
        verbose_name_plural = 'Лимиты банков'

    def __str__(self):
        return f'Лимиты банка {self.bank}'

    def clean(self):
        total = self.total_limit
        other = self.current_guaranties_sum + self.orders_sum
        if other > total:
            raise ValidationError("Указано некорректное ограничение")
        super(BankLimits, self).clean()

    def save(self, *args, **kwargs):
        super(BankLimits, self).save(*args, **kwargs)
        self.free_balance = self.total_limit - self.current_guaranties_sum - self.orders_sum
        super(BankLimits, self).save(*args, **kwargs)
