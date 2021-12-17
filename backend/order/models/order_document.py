from django.db import models
from garpix_page.utils.get_file_path import get_file_path

from app.mixins import Timestamps
from .order import Order


class OrderDocument(Timestamps):

    order = models.ForeignKey(Order, verbose_name='Заявка', on_delete=models.CASCADE, related_name='order_documents',
                              blank=False, null=False, default=None)
    document = models.FileField(verbose_name='Документ', upload_to=get_file_path, default='', blank=False, null=False)
    document_title = models.CharField(max_length=256, verbose_name='Название документа',
                                      blank=True, null=True, default='')
    document_type = models.ForeignKey('DocumentType', verbose_name='Тип документа', related_name='order_document_type',
                                      on_delete=models.CASCADE, null=True)
    is_valid = models.BooleanField(verbose_name='Валидный', blank=True, default=False)

    class Meta:
        verbose_name = 'Документ заявки'
        verbose_name_plural = 'Документы заявки'

    def __str__(self):
        return f'{self.order} - {self.document_type} - {self.document_title}'

    def save(self, *args, **kwargs):
        super(OrderDocument, self).save(*args, **kwargs)
        if not self.document_title or self.document_title == '':
            title = self.document.name.split('/')[-1]
            self.document_title = title
            super(OrderDocument, self).save(*args, **kwargs)
