from decimal import Decimal

from django.db import models

from app.mixins import Timestamps


class Ownership(Timestamps):
    title = models.CharField('Название', max_length=255)
    principal = models.ForeignKey('Principal', on_delete=models.CASCADE, related_name='ownership_principal',
                                  verbose_name='Принципал', null=True)
    co_owner = models.ForeignKey('CoOwner', on_delete=models.CASCADE, related_name='ownership_co_owner',
                                 verbose_name='Совладелец', null=True)
    fraction = models.DecimalField('Доля', max_digits=100, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Доля владения'
        verbose_name_plural = 'Доля владения'
