from django.db import models
from app.mixins import Timestamps


class BlackListItem(Timestamps):
    title = models.CharField(max_length=256, verbose_name='Название', blank=True)
    inn = models.CharField(max_length=12, verbose_name='Инн', unique=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True)

    class Meta:
        verbose_name = 'Элемент ЧС'
        verbose_name_plural = 'Черный список'

    def __str__(self):
        return self.title
