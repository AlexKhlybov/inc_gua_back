from decimal import Decimal
from django.db import models
from django.core.validators import RegexValidator

from app.mixins import Timestamps
from bank.models import BankGuaranteeStatus, Bank


class Guaranty(Timestamps):
    class TYPEGUARANTEE:
        ADVANCE = 'Аванс'
        TENDER = 'На участие в тендере'
        CONTRACT = 'На исполнение контракта'
        TYPES = (
            (ADVANCE, 'Аванс'),
            (TENDER, 'На участие в тендере'),
            (CONTRACT, 'На исполнение контракта'),
        )

    guarantee_type = models.CharField(max_length=100, verbose_name='Тип гарантии', choices=TYPEGUARANTEE.TYPES,
                                      blank=True, default='Аванс')
    bank = models.ForeignKey(Bank, verbose_name='Банк', on_delete=models.CASCADE, related_name='bank_guaranty',
                             blank=False, null=False, default=None)
    status = models.ForeignKey(BankGuaranteeStatus, verbose_name='Статус', blank=True, null=True, default=None,
                               on_delete=models.SET_DEFAULT, related_name='status_guaranty')
    sum = models.DecimalField(verbose_name='Сумма', max_digits=32, decimal_places=2, default=Decimal('0.00'))
    start_date = models.DateField(verbose_name='Дата начала действия гарантии', blank=True, null=True)
    end_date = models.DateField(verbose_name='Дата конца действия гарантии', blank=True, null=True)
    term = models.CharField(verbose_name='Срок гарантии(в днях)', blank=True, max_length=1000, validators=[
        RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры')], help_text='Пример: 365')
    take_date = models.DateField(verbose_name='Дата получения БГ', blank=True, null=True)
    availability_without_acceptance = models.BooleanField(verbose_name='Наличие права безакцептного списание',
                                                          blank=True, default=False)
    security_under_guarantee = models.BooleanField(verbose_name='Обеспечение по гарантии', blank=True, default=False)
    provision = models.BooleanField(verbose_name='Обеспечение', blank=True, default=False)
    provision_form = models.CharField(verbose_name='Форма обеспечения', blank=True, max_length=1000)
    provision_sum = models.DecimalField(verbose_name='Сумма обеспечения', max_digits=32, decimal_places=2,
                                        default=Decimal('0.00'))

    class Meta:
        verbose_name = 'Гарантия'
        verbose_name_plural = 'Гарантии'

    def __str__(self):
        return f'{self.sum} {self.take_date}'
