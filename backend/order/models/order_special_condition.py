from django.db import models

from app.mixins import Timestamps


class OrderSpecialCondition(Timestamps):

    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='')

    class Meta:
        verbose_name = 'Специальное условие'
        verbose_name_plural = 'Специальные условия'

    def __str__(self):
        return self.title
