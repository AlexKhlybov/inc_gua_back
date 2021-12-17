from django.db import models

from app.mixins import Timestamps


class AccountingForm(Timestamps):
    year = models.CharField(verbose_name='Год', max_length=100, blank=True)
    organization_type = models.CharField(verbose_name='Тип организации', max_length=100, blank=True)
    principal = models.ForeignKey('entity.Principal', on_delete=models.CASCADE, verbose_name='Принципал',
                                  related_name='accounting_form', null=True)

    class Meta:
        verbose_name = 'Бухгалтерская форма'
        verbose_name_plural = 'Бухгалтерские формы'

    def __str__(self):
        return f"{self.principal} - {self.organization_type} - {self.year}"
