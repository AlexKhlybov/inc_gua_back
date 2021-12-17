from django.db import models
from app.mixins import Timestamps


class Comment(Timestamps):
    content = models.TextField(verbose_name='Контент', default='')
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Заявка')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f"Комментарий к заявке{self.order}"
