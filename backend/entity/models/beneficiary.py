from django.db import models

from app.mixins import Timestamps
from .legal_entity import LegalEntity


class Beneficiary(Timestamps):
    title = models.CharField(max_length=256, verbose_name='Название')
    legal_entity = models.ForeignKey(LegalEntity, verbose_name='ЮЛ/ИП', on_delete=models.CASCADE,
                                     related_name='beneficiary_legal_entity',
                                     blank=False, null=False, default=None)

    class Meta:
        verbose_name = 'Бенефициар'
        verbose_name_plural = 'Бенефициар'

    def __str__(self):
        return f'{self.title}'
