from django.db import models
from decimal import Decimal

from app.mixins import Timestamps


class Contract(Timestamps):
    sum = models.DecimalField(verbose_name='Итоговая цена', max_digits=32, decimal_places=2, default=Decimal('0.00'))
    security_amount = models.DecimalField(verbose_name='Размер обеспечения', max_digits=32, decimal_places=2,
                                          default=Decimal('0.00'))
    term = models.DateField(verbose_name='Срок контракта', blank=True, null=True)
    availability_payment = models.BooleanField(verbose_name='Наличие аванса', default=False)
    availability_sum = models.DecimalField(verbose_name='Сумма аванса', max_digits=32, decimal_places=2,
                                           default=Decimal('0.00'))
    availability_share = models.DecimalField(verbose_name='Доля аванса в сумме контракта', max_digits=32,
                                             decimal_places=2, default=Decimal('0.00'))
    treasury_support = models.BooleanField(verbose_name='Казначейское сопровождение', default=False)
    number = models.CharField(verbose_name='Номер контракта', blank=True, max_length=1000)
    purchase = models.ForeignKey('Purchase', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Закупка')
    beneficiary = models.ForeignKey('entity.Beneficiary', on_delete=models.SET_NULL, null=True,
                                    verbose_name='Бенефициар')

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'

    def __str__(self):
        return f"Контракт номер {self.number} срок {self.term} сумма {self.sum}"
