from django.db import models

from app.mixins import Timestamps


class DocumentType(Timestamps):
    class TYPE:
        REGULATION = 'REGULATION'
        FINANCIAL = 'FINANCIAL'
        BUSINESS = 'BUSINESS'
        OTHER = 'OTHER'
        TYPES = (
            (REGULATION, 'REGULATION'),
            (FINANCIAL, 'FINANCIAL'),
            (BUSINESS, 'BUSINESS'),
            (OTHER, 'OTHER'),
        )

    type = models.CharField(max_length=100, verbose_name='Тип', choices=TYPE.TYPES,
                            blank=True, default='Прочие')
    title = models.CharField('Название', max_length=128)

    class Meta:
        verbose_name = 'Тип Документа'
        verbose_name_plural = 'Типы Документа'

    def __str__(self):
        return f'{self.title}'
