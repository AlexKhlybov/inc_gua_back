from django.db import models

from app.mixins import Timestamps


class Purchase(Timestamps):
    number = models.CharField(verbose_name='Номер Закупки', blank=True, max_length=1000)
    purchase_object = models.CharField(verbose_name='Предмет закупки', blank=True, max_length=1000)
    dumping = models.BooleanField(verbose_name='Дэмпинг', default=False)
    protocol_date = models.DateField(verbose_name='Дата протокола', blank=True, null=True)

    class Meta:
        verbose_name = 'Закупка'
        verbose_name_plural = 'Закупки'

    def __str__(self):
        return f'{self.purchase_object}'
