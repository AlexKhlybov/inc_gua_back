from django.db import models

from app.mixins import Timestamps
from ..mixins.alarm import AlarmMixin


class StopFactor(AlarmMixin, Timestamps):

    stop_factor_exception = models.TextField(verbose_name='Исключения', blank=True, null=True, default='')

    class Meta:
        verbose_name = 'Стоп-фактор'
        verbose_name_plural = 'Стоп-факторы'

    def __str__(self):
        return self.description
