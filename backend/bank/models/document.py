from django.db import models
from app.mixins import Timestamps
from garpix_page.utils.get_file_path import get_file_path


class Document(Timestamps):
    title = models.CharField(max_length=256, verbose_name='Название', default='')
    is_loaded = models.BooleanField(default=False, verbose_name='Загружено?')
    document = models.FileField(verbose_name='Документ', upload_to=get_file_path, default='', blank=False, null=False)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.title
