from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def check_value_len(value, _min, _max):
    """change to the django.core.validators.MinLengthValidator and django.core.validators.MaxLengthValidator"""
    _value = str(value)
    if len(_value) < _min:
        raise ValidationError(_(f'minimum number of characters {_min}'))
    elif len(_value) > _max:
        raise ValidationError(_(f'maximum number of characters {_max}'))
    else:
        return True


def check_value_is_alpha(value):
    """change to the django.core.validators.RegexValidator(r'^[a-zA-Zа-яА-ЯёЁ-]*$', 'Специальные символы не допускаются, за исключением "-"')"""
    checked_str = str(value).replace('-', '')
    if checked_str.isalpha():
        return True
    else:
        raise ValidationError(_('cпециальные символы не допускаются, за исключением "-"'))


def check_value_is_digit(value):
    """change to the django.core.validators.RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры')"""
    if value.isdigit():
        return True
    else:
        raise ValidationError(_('the value must be numeric'))
