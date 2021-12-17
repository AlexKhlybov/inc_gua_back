from django.db import models

from app.mixins import Timestamps


class AccountingFormDetail(Timestamps):
    code = models.CharField(verbose_name='Код строки', max_length=100, blank=True, null=True)
    line_name = models.CharField(verbose_name='Название строки', max_length=300, blank=True, null=True)
    start_value = models.BigIntegerField(verbose_name='Значение на начало периода',
                                         blank=True, null=True)
    end_value = models.BigIntegerField(verbose_name='Значение на конец периода',
                                       blank=True, null=True)
    accounting_form = models.ForeignKey('AccountingForm', on_delete=models.CASCADE, related_name='detail_form',
                                        verbose_name='Форма', null=True)

    class Meta:
        verbose_name = 'Детальная бухгалтерская форма'
        verbose_name_plural = 'Детальные бухгалтерские формы'

    def __str__(self):
        return f'{self.accounting_form} - {self.line_name}'
