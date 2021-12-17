from decimal import Decimal

from django.db import models

from app.mixins import Timestamps


class CoOwner(Timestamps):
    title = models.CharField('Название', max_length=255)
    fraction = models.DecimalField('Значение доли', max_digits=100, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Совладелец'
        verbose_name_plural = 'Совладельцы'
