from django.db import models

from app.mixins import Timestamps


class Auction(Timestamps):
    number = models.CharField(verbose_name='Номер торга', blank=True, max_length=1000)

    class Meta:
        verbose_name = 'Торг'
        verbose_name_plural = 'Торги'

    def __str__(self):
        return f"Торг номер {self.number}"
