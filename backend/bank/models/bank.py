from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils.translation import gettext as _

from garpix_page.utils.get_file_path import get_file_path
from app.mixins import Timestamps


class Bank(Timestamps):
    title = models.CharField(max_length=128, verbose_name='Название', default='')
    inn = models.CharField(max_length=12, verbose_name='ИНН', blank=True, null=True,
                           validators=[
                               RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                               MinLengthValidator(10, _('Min value should consist of at least 10 characters')),
                               MaxLengthValidator(12, _('Max value must not contain more than 12 characters')),
                           ])
    registration_address = models.CharField(max_length=264, verbose_name='Адрес регистрации', blank=True,
                                            help_text='Пример: Индекс Город, Улица, Дом, Помещение')
    bik = models.CharField(max_length=9, verbose_name='БИК', blank=True,
                           validators=[
                               RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                               MinLengthValidator(9, _('Min value should consist of at least 9 characters')),
                               MaxLengthValidator(9, _('Max value must not contain more than 9 characters')),
                           ])
    kpp = models.CharField(max_length=9, verbose_name='КПП', blank=True,
                           validators=[
                               RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                               MinLengthValidator(9, _('Min value should consist of at least 9 characters')),
                               MaxLengthValidator(9, _('Max value must not contain more than 9 characters')),
                           ])
    correspondent_account_cb = models.CharField(
        max_length=20, verbose_name='Корреспондентский счет в ЦБ', blank=True,
        validators=[
            RegexValidator(r'^[0-9]*$',
                           'Значение должно содержать только цифры'),
            MinLengthValidator(20, _('Min value should consist of at least 20 characters')),
            MaxLengthValidator(20, _('Max value must not contain more than 20 characters')),
        ])
    registration_date = models.DateField(verbose_name='Дата регистрации', blank=True, null=True)

    region = models.CharField(max_length=264, verbose_name='Регион', blank=True, help_text='Пример: 00 - Регион')
    license_number = models.CharField(max_length=264, verbose_name='Номер лицензии', blank=True,
                                      validators=[RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                                                  ])
    eio_surname = models.CharField(max_length=264, verbose_name='ЕИО / Фамилия', blank=True, validators=[
        RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'),
        MinLengthValidator(2, _('Min value should consist of at least 2 characters')),
        MaxLengthValidator(22, _('Max value must not contain more than 22 characters'))], )
    eio_name = models.CharField(max_length=264, verbose_name='ЕИО / Имя', blank=True, validators=[
        RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'),
        MinLengthValidator(2, _('Min value should consist of at least 2 characters')),
        MaxLengthValidator(22, _('Max value must not contain more than 22 characters'))], )
    eio_patronymic = models.CharField(max_length=264, verbose_name='ЕИО / Отчество', blank=True, validators=[
        RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'),
        MinLengthValidator(2, _('Min value should consist of at least 2 characters')),
        MaxLengthValidator(22, _('Max value must not contain more than 22 characters'))], )
    eio_appointment_date = models.DateField(verbose_name='Дата назначения ЕИО', blank=True, null=True)

    contact_person_surname = models.CharField(
        max_length=264, verbose_name='Контактное лицо / Фамилия', blank=True,
        validators=[
            RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'),
            MinLengthValidator(2, _('Min value should consist of at least 2 characters')),
            MaxLengthValidator(22, _('Max value must not contain more than 22 characters'))], )
    contact_person_name = models.CharField(
        max_length=264, verbose_name='Контактное лицо / Имя', blank=True,
        validators=[
            RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'),
            MinLengthValidator(2, _('Min value should consist of at least 2 characters')),
            MaxLengthValidator(22, _('Max value must not contain more than 22 characters'))], )
    contact_patronymic = models.CharField(
        max_length=264, verbose_name='Контактное лицо / Отчество', blank=True,
        validators=[
            RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'),
            MinLengthValidator(2, _('Min value should consist of at least 2 characters')),
            MaxLengthValidator(22, _('Max value must not contain more than 22 characters'))], )

    email = models.EmailField(verbose_name='Эл. почта', blank=True)
    phone = models.CharField(max_length=30, blank=True, default='', verbose_name='Телефон',
                             validators=[
                                 RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                                 MinLengthValidator(11, _('Min value should consist of at least 11 characters')),
                                 MaxLengthValidator(11, _('Max value must not contain more than 11 characters')),
                             ])
    logo = models.FileField(verbose_name='Лого', upload_to=get_file_path, default='', blank=True)

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'

    def __str__(self):
        return self.title

    @property
    def get_logo_url(self):
        return settings.SITE_URL + self.logo.url if self.logo else '#'
