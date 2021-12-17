from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils.translation import gettext as _

from app.mixins import Timestamps
from ..mixins import PassportMixin


class Person(PassportMixin, Timestamps):
    last_name = models.CharField(verbose_name='Фамилия', max_length=150, blank=True,
                                 validators=[
                                     RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ ]*$',
                                                    'Специальные символы не допускаются, за исключением "-"'),
                                     MinLengthValidator(2, _('Min value should consist of at least 2 characters')),
                                     MaxLengthValidator(22, _('Max value must not contain more than 22 characters')),
                                 ])
    first_name = models.CharField(verbose_name='Имя', max_length=150, blank=True,
                                  validators=[
                                      RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ-]*$',
                                                     'Специальные символы не допускаются, за исключением "-"'),
                                      MinLengthValidator(2, _('Min value should consist of at least 2 characters')),
                                      MaxLengthValidator(22, _('Max value must not contain more than 22 characters')),
                                  ])
    patronymic = models.CharField(max_length=150, verbose_name='Отчество', blank=True,
                                  validators=[
                                      RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ-]*$',
                                                     'Специальные символы не допускаются, за исключением "-"'),
                                      MinLengthValidator(2, _('Min value should consist of at least 2 characters')),
                                      MaxLengthValidator(22, _('Max value must not contain more than 22 characters')),
                                  ])
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    birth_place = models.CharField(max_length=300, verbose_name='Место рождения', blank=True)

    class Meta:
        verbose_name = 'Физическое лицо'
        verbose_name_plural = 'Физические лица'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'
