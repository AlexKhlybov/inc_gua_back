# Generated by Django 3.1 on 2021-09-30 14:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0024_auto_20210928_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalentity',
            name='bank_bik',
            field=models.CharField(blank=True, max_length=264, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(9, 'Min value should consist of at least 9 characters'), django.core.validators.MaxLengthValidator(9, 'Max value must not contain more than 9 characters')], verbose_name='БИК банка'),
        ),
        migrations.AlterField(
            model_name='legalentity',
            name='bank_correspondent_account_cb',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(20, 'Min value should consist of at least 20 characters'), django.core.validators.MaxLengthValidator(20, 'Max value must not contain more than 22 characters')], verbose_name='Корреспондентский счет в ЦБ'),
        ),
        migrations.AlterField(
            model_name='legalentity',
            name='bank_inn',
            field=models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(10, 'Min value should consist of at least 10 characters'), django.core.validators.MaxLengthValidator(12, 'Max value must not contain more than 12 characters')], verbose_name='ИНН банка'),
        ),
        migrations.AlterField(
            model_name='legalentity',
            name='bank_kpp',
            field=models.CharField(blank=True, max_length=264, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(9, 'Min value should consist of at least 9 characters'), django.core.validators.MaxLengthValidator(9, 'Max value must not contain more than 9 characters')], verbose_name='КПП банка'),
        ),
        migrations.AlterField(
            model_name='legalentity',
            name='bank_number',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(20, 'Min value should consist of at least 20 characters'), django.core.validators.MaxLengthValidator(20, 'Max value must not contain more than 20 characters')], verbose_name='Банковский счет'),
        ),
        migrations.AlterField(
            model_name='legalentity',
            name='inn',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(10, 'Min value should consist of at least 10 characters'), django.core.validators.MaxLengthValidator(12, 'Max value must not contain more than 12 characters')], verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='legalentity',
            name='kpp',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(10, 'Min value should consist of at least 10 characters'), django.core.validators.MaxLengthValidator(10, 'Max value must not contain more than 10 characters')], verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='legalentity',
            name='okved',
            field=models.CharField(help_text='Пример формата ввода: XX.XX.XX, XX.XX', max_length=8, validators=[django.core.validators.RegexValidator('^([\\s\\.]?[0-9]+)+$', 'Значение должно содержать цифры и точку'), django.core.validators.MinLengthValidator(2, 'Min value should consist of at least 2 characters'), django.core.validators.MaxLengthValidator(8, 'Max value must not contain more than 8 characters')], verbose_name='ОКВЭД (Основные)'),
        ),
        migrations.AlterField(
            model_name='legalentity',
            name='title',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[а-яА-ЯёЁ\\s]+$', 'Значение должно содержать только кириллицу')], verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='person',
            name='department_code',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(6, 'Min value should consist of at least 6 characters'), django.core.validators.MaxLengthValidator(6, 'Max value must not contain more than 6 characters')], verbose_name='Код подразделения'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ-]*$', 'Специальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2, 'Min value should consist of at least 2 characters'), django.core.validators.MaxLengthValidator(22, 'Max value must not contain more than 22 characters')], verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ ]*$', 'Специальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2, 'Min value should consist of at least 2 characters'), django.core.validators.MaxLengthValidator(22, 'Max value must not contain more than 22 characters')], verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='person',
            name='passport_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(6, 'Min value should consist of at least 6 characters'), django.core.validators.MaxLengthValidator(6, 'Max value must not contain more than 6 characters')], verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='person',
            name='passport_series',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(4, 'Min value should consist of at least 4 characters'), django.core.validators.MaxLengthValidator(4, 'Max value must not contain more than 4 characters')], verbose_name='Серия паспорта'),
        ),
        migrations.AlterField(
            model_name='person',
            name='patronymic',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ-]*$', 'Специальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2, 'Min value should consist of at least 2 characters'), django.core.validators.MaxLengthValidator(22, 'Max value must not contain more than 22 characters')], verbose_name='Отчество'),
        ),
    ]
