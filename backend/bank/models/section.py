from django.db import models
from app.mixins import Timestamps
from .document import Document


class Section(Timestamps):
    title = models.CharField(max_length=256, verbose_name='Название', default='')
    document = models.ManyToManyField(Document, verbose_name='Документ',
                                      related_name='section_document', blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title
