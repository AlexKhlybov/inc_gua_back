from django.db import models

from app.mixins import Timestamps
from .bank import Bank


class BankTariffMatrix(Timestamps):

    bank = models.OneToOneField(Bank, verbose_name='Банк', related_name='bank_tariff_matrix', blank=False, null=False,
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Матрица тарифов банка'
        verbose_name_plural = 'Матрицы тарифов банка'

    def __str__(self):
        return f'Матрица тарифов банка {self.bank}'

    def get_matrix(self):
        return {}
