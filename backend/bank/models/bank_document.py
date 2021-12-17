from django.conf import settings
from django.db import models
from garpix_page.utils.get_file_path import get_file_path
from app.mixins import Timestamps
from .bank import Bank


class BankDocument(Timestamps):

    bank = models.ForeignKey(Bank, verbose_name='Банк', on_delete=models.CASCADE, related_name='bank_documents',
                             blank=False, null=False, default=None)
    document = models.FileField(verbose_name='Документ', upload_to=get_file_path, default='', blank=False, null=False)
    document_title = models.CharField(max_length=256, verbose_name='Название документа',
                                      blank=True, null=True, default='')
    document_type = models.ForeignKey('order.DocumentType', verbose_name='Тип Документа', on_delete=models.CASCADE,
                                      related_name='bank_document_type', default=None)

    class Meta:
        verbose_name = 'Документ банка'
        verbose_name_plural = 'Документы банка'

    def __str__(self):
        return f'{self.bank} - {self.document_type} - {self.document_title}'

    def save(self, *args, **kwargs):
        super(BankDocument, self).save(*args, **kwargs)
        if not self.document_title or self.document_title == '':
            title = self.document.name.split('/')[-1]
            self.document_title = title
            super(BankDocument, self).save(*args, **kwargs)

    @property
    def get_document_url(self):
        return settings.SITE_URL + self.document.url if self.document else '#'
