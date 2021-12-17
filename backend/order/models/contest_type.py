from django.db import models

from app.mixins import Timestamps


class ContestType(Timestamps):
    title = models.CharField(verbose_name='Название', blank=True, max_length=1000)

    class Meta:
        verbose_name = 'Тип конкурса'
        verbose_name_plural = 'Типы конкурса'

    def __str__(self):
        return self.title
