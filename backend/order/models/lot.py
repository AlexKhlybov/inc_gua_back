from django.db import models

from app.mixins import Timestamps


class Lot(Timestamps):
    number = models.CharField(verbose_name='Номер лота', blank=True, max_length=1000)

    class Meta:
        verbose_name = 'Лот'
        verbose_name_plural = 'Лоты'

    def __str__(self):
        return f"Лот номер {self.number}"
