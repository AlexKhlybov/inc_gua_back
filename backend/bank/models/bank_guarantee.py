# from decimal import Decimal
# from django.db import models

from app.mixins import Timestamps
# from .bank_guarantee_status import BankGuaranteeStatus
# from .bank import Bank


class BankGuarantee(Timestamps):
    # bank = models.ForeignKey(Bank, verbose_name='Банк', on_delete=models.CASCADE, related_name='bank_guarantee',
    #                          blank=False, null=False, default=None)
    # status = models.ForeignKey(BankGuaranteeStatus, verbose_name='Статус', blank=True, null=True, default=None,
    #                            on_delete=models.SET_DEFAULT, related_name='status')
    # number = models.CharField(max_length=128, verbose_name='Номер', blank=True, default='')
    # date = models.DateField(verbose_name='Дата', blank=True, null=True)
    # maintain_a_guarantee = models.TextField(max_length=500, verbose_name='Обязательства по гарантии', blank=True, null=True, default='')
    # sum = models.DecimalField(verbose_name='Сумма гарантии', max_digits=32, decimal_places=2, default=Decimal('0.00'), blank=True)
    # disclosure_conditions = models.TextField(max_length=500, verbose_name='Условия раскрытия БГ', blank=True, null=True, default='')
    # rights_and_liabilities_of_the_parties = models.TextField(max_length=500, verbose_name='Права и обязанности сторон', blank=True, null=True, default='')
    # termination_of_liabilities = models.TextField(max_length=500, verbose_name='Прекращение обязательств', blank=True, null=True, default='')
    pass

    class Meta:
        verbose_name = 'Банковская гарантия'
        verbose_name_plural = 'Банковские гарантии'

    def __str__(self):
        return f'{self.number} - {self.date}'
