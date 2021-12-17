from django.db import models
from app.mixins import Timestamps
from .bank import Bank


class BankСontract(Timestamps):
    bank = models.ForeignKey(Bank, verbose_name='Банк', on_delete=models.CASCADE, related_name='bank_contract',
                             blank=False, null=False, default=None)
    summary_protocol_name = models.CharField(max_length=500, verbose_name='Наименование протокола итогов', default='')
    summary_protocol_number = models.CharField(max_length=128, verbose_name='Номер протокола итогов', default='')
    summary_protocol_date = models.DateField(verbose_name='Дата протокола итогов', blank=True, null=True)
    subject_of_contract = models.TextField(max_length=500, verbose_name='Предмет контракта', default='')

    class Meta:
        verbose_name = 'Контракт банка'
        verbose_name_plural = 'Контракты банка'

    def __str__(self):
        return f'{self.summary_protocol_number} - {self.summary_protocol_date}'
