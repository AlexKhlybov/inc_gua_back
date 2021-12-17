from django.db import models
from garpix_utils.file import get_file_path

from app.mixins import Timestamps


class Document(Timestamps):
    title = models.CharField(max_length=500, verbose_name='Название', unique=True)
    document = models.FileField(verbose_name="Документ", upload_to=get_file_path)
    principal = models.ForeignKey('Principal', on_delete=models.CASCADE, related_name='principal_document',
                                  verbose_name='Принципал')

    def __str__(self):
        return f'{self.title} {self.principal}'

    class Meta:
        verbose_name = 'Документ Принципала'
        verbose_name_plural = 'Документы Принципала'
