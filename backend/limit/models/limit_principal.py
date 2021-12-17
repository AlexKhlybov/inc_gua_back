from decimal import Decimal
from django.db import models
from django.core.exceptions import ValidationError

from app.mixins import Timestamps
from entity.models import Principal


class LimitPrincipalModel(Timestamps):
    principal = models.OneToOneField(Principal, on_delete=models.CASCADE, related_name='limit_principal', blank=False,
                                     null=False, verbose_name='Принципал', default=None)
    limit = models.DecimalField(verbose_name='Лимит', max_digits=32, decimal_places=2, default=Decimal('0.00'))
    total_limit = models.DecimalField(verbose_name='Установленный лимит', max_digits=32, decimal_places=2,
                                      default=Decimal('0.00'))
    current_guaranties_sum = models.DecimalField(verbose_name='Действующие БГ', max_digits=32, decimal_places=2,
                                                 default=Decimal('0.00'))
    orders_sum = models.DecimalField(verbose_name='Общая сумма заявок', max_digits=32, decimal_places=2, default=Decimal('0.00'))
    free_balance = models.DecimalField(verbose_name='Свободный остаток', max_digits=32, decimal_places=2,
                                       default=Decimal('0.00'))

    class Meta:
        verbose_name = 'Установленный лимит принципала'
        verbose_name_plural = 'Установленные лимиты принципалов'

    def __str__(self):
        return f'Принципал - {self.principal} - {self.limit}'

    def clean(self):
        total = self.total_limit
        other = self.current_guaranties_sum + self.orders_sum
        if other > total:
            raise ValidationError("Указано некорректное ограничение")
        super(LimitPrincipalModel, self).clean()

    def save(self, *args, **kwargs):
        super(LimitPrincipalModel, self).save(*args, **kwargs)
        self.total_limit = self.limit if self.total_limit == 0 else self.total_limit
        self.free_balance = self.total_limit - self.current_guaranties_sum - self.orders_sum
        super(LimitPrincipalModel, self).save(*args, **kwargs)
