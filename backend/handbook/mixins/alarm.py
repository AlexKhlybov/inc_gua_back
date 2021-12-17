from django.db import models


class AlarmMixin(models.Model):

    description = models.TextField(verbose_name='Описание', blank=False, null=False, default='')
    is_active = models.BooleanField(verbose_name='Активно', default=True)

    class Meta:
        abstract = True
