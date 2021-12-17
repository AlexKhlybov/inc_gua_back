from django.db import models
from django.core.validators import RegexValidator

from app.mixins import Timestamps


class Contest(Timestamps):
    lot = models.ForeignKey('Lot', on_delete=models.CASCADE, verbose_name='Лот')
    type = models.ForeignKey('ContestType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Тип')
    contract = models.ForeignKey('Contract', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Контракт')
    defined = models.BooleanField(verbose_name='Определен?', default=False)
    fz = models.ForeignKey('limit.LimitFZ', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='ФЗ',
                           related_name='fz_contest')
    okpd2 = models.CharField(max_length=1000, blank=True, verbose_name='ОКПД2')
    nmck = models.CharField(max_length=1000, blank=True, verbose_name='НМЦК', validators=[
        RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
    ])
    purchase = models.ForeignKey('Purchase', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Закупка')

    class Meta:
        verbose_name = 'Конкурс'
        verbose_name_plural = 'Конкурсы'

    def __str__(self):
        return f"{self.type} {self.nmck}"
