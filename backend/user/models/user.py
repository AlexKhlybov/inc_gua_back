import string
from django.contrib.auth.models import AbstractUser
from garpix_notify.mixins import UserNotifyMixin
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils.translation import gettext as _

from app.mixins import Timestamps
from garpix_notify.utils import get_file_path

from .manager import CustomUserManager
from .pages.change_password import ChangePassword


class User(AbstractUser, UserNotifyMixin, Timestamps):
    class ROLE:
        UNDERWRITER = 'Андеррайтер'
        MASTER_UNDERWRITER = 'Мастер-андеррайтер'
        PRINCIPAL = 'Принципал'
        AGENT = 'Агент'
        BANK = 'Банк'
        TYPES = (
            (UNDERWRITER, 'Андеррайтер'),
            (MASTER_UNDERWRITER, 'Мастер-андеррайтер'),
            (PRINCIPAL, 'Принципал'),
            (AGENT, 'Агент'),
            (BANK, 'Банк'),
        )

    username = None
    email = models.EmailField(verbose_name='Адрес электронной почты', unique=True)
    role = models.CharField(max_length=100, verbose_name='Роль', choices=ROLE.TYPES, default='Андеррайтер')
    first_name = models.CharField(verbose_name='Имя', max_length=150,
                                  validators=[
                                      RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ-]*$',
                                                     'Cпециальные символы не допускаются, за исключением "-"'),
                                      MinLengthValidator(2, _('Min value should consist of at least 2 characters')),
                                      MaxLengthValidator(22, _('Max value must not contain more than 22 characters')),
                                  ])
    last_name = models.CharField(verbose_name='Фамилия', max_length=150,
                                 validators=[
                                     RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ-]*$',
                                                    'Cпециальные символы не допускаются, за исключением "-"'),
                                     MinLengthValidator(2, _('Min value should consist of at least 2 characters')),
                                     MaxLengthValidator(22, _('Max value must not contain more than 22 characters')),
                                 ])
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', blank=True,
                                  validators=[
                                      RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ-]*$',
                                                     'Cпециальные символы не допускаются, за исключением "-"'),
                                      MinLengthValidator(2, _('Min value should consist of at least 2 characters')),
                                      MaxLengthValidator(22, _('Max value must not contain more than 22 characters')),
                                  ])
    password_reset_key = models.CharField(max_length=216, default="", verbose_name="Ссылка для сброса пароля",
                                          blank=True)
    attempts = models.IntegerField("Неудачных попыток", default=0)
    authority = models.DecimalField('Полномочия', max_digits=32, decimal_places=2, default='0.00', blank=True,
                                    null=True)

    logo = models.FileField(verbose_name='Лого', upload_to=get_file_path, default='', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    def generate_link(self):
        change_password_page = ChangePassword.objects.first()
        if not change_password_page:
            change_password_page = ChangePassword.objects.create(title='default')
        page_url = change_password_page.get_absolute_url()
        site_url = change_password_page.get_sites
        import random
        letters = string.ascii_letters
        result = f'{site_url}{page_url}/?reset_code=' + ''.join(random.choice(letters) for i in range(64))
        if page_url:
            self.password_reset_key = result.replace(" ", "")
            self.save()
            return self.password_reset_key
