from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils.translation import gettext as _

from app.mixins import Timestamps
from .person import Person


class LegalEntity(Timestamps):
    class TYPE:
        IP = 'Индивидуальный предприниматель'
        UL = 'Юридическое лицо'
        TYPES = (
            (IP, 'Индивидуальный предприниматель'),
            (UL, 'Юридическое лицо'),
        )

    class TAXATION:
        OSN = 'ОСН'
        USN = 'УСН'
        ESHN = 'ЕСХР'
        ENVD = 'ЕНВД'
        PSN = 'ПСН'
        TYPES = (
            (OSN, 'ОСН'),
            (USN, 'УСН'),
            (ESHN, 'ЕСХР'),
            (ENVD, 'ЕНВД'),
            (PSN, 'ПСН'),
        )

    title = models.CharField(max_length=256,
                             validators=[RegexValidator(
                                 r'^[а-яА-ЯёЁ\s. -0-9ivxcdlIVXCDL:]+$',
                                 'Значение должно содержать только кириллицу, цифры, римские цифры')],
                             verbose_name='Название')
    other_title = models.CharField(max_length=256, verbose_name='Другое Название', blank=True, null=True)
    type = models.CharField(max_length=100, verbose_name='Тип', choices=TYPE.TYPES, default=TYPE.TYPES[1])
    taxation = models.CharField(max_length=100, verbose_name='Налогообложение', choices=TAXATION.TYPES,
                                default=TAXATION.TYPES[0])
    inn = models.CharField(max_length=12, verbose_name='ИНН',
                           validators=[
                               RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                               MinLengthValidator(10, _('Min value should consist of at least 10 characters')),
                               MaxLengthValidator(12, _('Max value must not contain more than 12 characters')),

                           ])
    kpp = models.CharField(max_length=10, verbose_name='КПП',
                           validators=[
                               RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                               MinLengthValidator(9, _('Min value should consist of at least 9 characters')),
                               MaxLengthValidator(9, _('Max value must not contain more than 9 characters')),
                           ])
    registration_date = models.DateField(verbose_name='Дата регистрации', blank=True, null=True)
    registration_address = models.CharField(max_length=400, verbose_name='Адрес регистрации', blank=True)
    actual_address = models.CharField(max_length=400, verbose_name='Фактический адрес', blank=True)
    okved = models.CharField(max_length=8, help_text='Пример формата ввода: XX.XX.XX, XX.XX',
                             validators=[
                                 RegexValidator(r'^([\s\.]?[0-9]+)+$', 'Значение должно содержать цифры и точку'),
                                 MinLengthValidator(2, _('Min value should consist of at least 2 characters')),
                                 MaxLengthValidator(8, _('Max value must not contain more than 8 characters')),
                             ],
                             verbose_name='ОКВЭД (Основные)')
    region = models.CharField(max_length=128, verbose_name='Регион')
    opf = models.CharField(max_length=256, verbose_name='Организационно-правовая форма', blank=True)
    average_number_of_employees = models.PositiveIntegerField(verbose_name='Среднесписочная численность', null=True,
                                                              blank=True)
    regulation_document = models.CharField(max_length=256, verbose_name='Устав', blank=True, null=True)
    attorney_document = models.CharField(max_length=256, verbose_name='Доверенность', blank=True, null=True)

    bank_number = models.CharField(max_length=20, verbose_name='Банковский счет', blank=True, null=True,
                                   validators=[
                                       RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                                       MinLengthValidator(20, _('Min value should consist of at least 20 characters')),
                                       MaxLengthValidator(20, _('Max value must not contain more than 20 characters')),
                                   ])
    bank_name = models.CharField(max_length=128, verbose_name='Название банка', blank=True, default='')
    bank_inn = models.CharField(max_length=12, verbose_name='ИНН банка', blank=True, null=True,
                                validators=[
                                    RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                                    MinLengthValidator(10, _('Min value should consist of at least 10 characters')),
                                    MaxLengthValidator(12, _('Max value must not contain more than 12 characters')),
                                ])
    bank_bik = models.CharField(max_length=264, verbose_name='БИК банка', blank=True,
                                validators=[
                                    RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                                    MinLengthValidator(9, _('Min value should consist of at least 9 characters')),
                                    MaxLengthValidator(9, _('Max value must not contain more than 9 characters')),
                                ])
    bank_kpp = models.CharField(max_length=264, verbose_name='КПП банка', blank=True,
                                validators=[
                                    RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                                    MinLengthValidator(9, _('Min value should consist of at least 9 characters')),
                                    MaxLengthValidator(9, _('Max value must not contain more than 9 characters')),
                                ])
    bank_correspondent_account_cb = models.CharField(
        max_length=20, verbose_name='Корреспондентский счет в ЦБ', blank=True, validators=[
            RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
            MinLengthValidator(20, _('Min value should consist of at least 20 characters')),
            MaxLengthValidator(20, _('Max value must not contain more than 22 characters')),
        ])

    fl = models.ForeignKey(Person, verbose_name='Физическое лицо', on_delete=models.CASCADE,
                           related_name='legal_entity_fl', blank=True, null=True)
    eio = models.ForeignKey(Person, verbose_name='Единоличный исполнительный орган', on_delete=models.CASCADE,
                            related_name='legal_entity_eio', blank=True, null=True)
    eio_date = models.DateField(verbose_name='Дата назначения ЕИО', blank=True, null=True)
    lpr = models.ForeignKey(Person, verbose_name='Лицо, принимающее решения', on_delete=models.CASCADE,
                            related_name='legal_entity_lpr', blank=True, null=True)
    lpr_post = models.CharField(max_length=128, verbose_name='Должность ЛПР', blank=True, default='')
    auditor = models.ForeignKey(Person, verbose_name='Аудитор', on_delete=models.CASCADE,
                                related_name='legal_entity_auditor', blank=True, null=True)
    auditor_opinion = models.CharField(max_length=128, verbose_name='Мнение аудитора', blank=True, default='')

    no_audit = models.BooleanField(verbose_name='Аудит не проводится', default=False)

    class Meta:
        verbose_name = 'Юридическое лицо / ИП'
        verbose_name_plural = 'Юридические лица / ИП'

    def __str__(self):
        return f'{self.opf} {self.title} - {self.inn}'

    def clean(self):
        if self.type == 'Индивидуальный предприниматель' and len(self.inn) != 12:
            raise ValidationError(_('the TIN field of an individual entrepreneur must consist of 12 characters'))
        if self.type == 'Юридическое лицо' and len(self.inn) != 10:
            raise ValidationError(_('the TIN field of a legal entity must consist of 10 characters'))
