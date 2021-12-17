from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils.translation import gettext as _


class PassportMixin(models.Model):
    passport_series = models.CharField(
        max_length=10, verbose_name='Серия паспорта', blank=True,
        validators=[
            RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
            MinLengthValidator(4, _('Min value should consist of at least 4 characters')),
            MaxLengthValidator(4, _('Max value must not contain more than 4 characters')), ])
    passport_number = models.CharField(max_length=10, verbose_name='Номер паспорта', blank=True,
                                       validators=[
                                           RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                                           MinLengthValidator(6, _('Min value should consist of at least 6 characters')),
                                           MaxLengthValidator(6, _('Max value must not contain more than 6 characters')),
                                       ])
    department_code = models.CharField(max_length=10, verbose_name='Код подразделения', blank=True,
                                       validators=[
                                           RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                                           MinLengthValidator(6, _('Min value should consist of at least 6 characters')),
                                           MaxLengthValidator(6, _('Max value must not contain more than 6 characters')),
                                       ])
    collect_date = models.DateField(verbose_name='Дата выдачи', blank=True, null=True)
    collect_by_whom = models.CharField(max_length=200, verbose_name='Кем выдан', blank=True)
    registration_address = models.CharField(max_length=400, verbose_name='Адрес регистрации', blank=True)
    citizenship = models.CharField(max_length=400, verbose_name='Гражданство', blank=True)

    class Meta:
        abstract = True
