from django.db import models
from solo.models import SingletonModel

DEFAULT_PRIVATE_KEY = ''''''
DEFAULT_PUBLIC_KEY = ''''''


class SiteConfiguration(SingletonModel):
    private_key = models.TextField(default=DEFAULT_PRIVATE_KEY, verbose_name='Приватный ключ')
    public_key = models.TextField(default=DEFAULT_PUBLIC_KEY, verbose_name='Публичный ключ')
    limit_to_retry = models.IntegerField(default=5, verbose_name='Количество попыток запросов интеграций')

    def __str__(self):
        return 'Site Configuration'

    class Meta:
        verbose_name = "Конфигурация сайта"
