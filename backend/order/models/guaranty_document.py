from django.db import models
from garpix_page.utils.get_file_path import get_file_path

from app.mixins import Timestamps
from .guaranty import Guaranty


class GuarantyDocument(Timestamps):
    guaranty = models.ForeignKey(Guaranty, verbose_name='Гарантия', on_delete=models.CASCADE,
                                 related_name='guaranty_documents', blank=False, null=False, default=None)
    document = models.FileField(verbose_name='Документ', upload_to=get_file_path, default='', blank=False, null=False)
    document_title = models.CharField(max_length=256, verbose_name='Название документа', blank=True, null=True,
                                      default='')
    document_type = models.ForeignKey('DocumentType', verbose_name='Тип документа',
                                      related_name='guaranty_document_type', on_delete=models.CASCADE, null=True)
    is_valid = models.BooleanField(verbose_name='Валидный', blank=True, default=False)

    class Meta:
        verbose_name = 'Документ гарантии'
        verbose_name_plural = 'Документы гарантии'

    def __str__(self):
        return f'{self.guaranty} - {self.document_type} - {self.document_title}'

    def save(self, *args, **kwargs):
        super(GuarantyDocument, self).save(*args, **kwargs)
        if not self.document_title or self.document_title == '':
            title = self.document.name.split('/')[-1]
            self.document_title = title
            super(GuarantyDocument, self).save(*args, **kwargs)
