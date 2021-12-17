from django.db import models


class Timestamps(models.Model):
    create_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True, blank=True, null=True)
    update_at = models.DateTimeField(verbose_name='Изменено', auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True
