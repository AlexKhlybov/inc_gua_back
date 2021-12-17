# Generated by Django 3.1 on 2021-09-30 14:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0019_auto_20210928_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bik',
            field=models.CharField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(9, 'Min value should consist of at least 9 characters'), django.core.validators.MaxLengthValidator(9, 'Max value must not contain more than 9 characters')], verbose_name='БИК'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='contact_patronymic',
            field=models.CharField(blank=True, max_length=264, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2, 'Min value should consist of at least 2 characters'), django.core.validators.MaxLengthValidator(22, 'Max value must not contain more than 22 characters')], verbose_name='Контактное лицо / Отчество'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='contact_person_name',
            field=models.CharField(blank=True, max_length=264, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2, 'Min value should consist of at least 2 characters'), django.core.validators.MaxLengthValidator(22, 'Max value must not contain more than 22 characters')], verbose_name='Контактное лицо / Имя'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='contact_person_surname',
            field=models.CharField(blank=True, max_length=264, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2, 'Min value should consist of at least 2 characters'), django.core.validators.MaxLengthValidator(22, 'Max value must not contain more than 22 characters')], verbose_name='Контактное лицо / Фамилия'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='correspondent_account_cb',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(20, 'Min value should consist of at least 20 characters'), django.core.validators.MaxLengthValidator(20, 'Max value must not contain more than 20 characters')], verbose_name='Корреспондентский счет в ЦБ'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='eio_name',
            field=models.CharField(blank=True, max_length=264, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2, 'Min value should consist of at least 2 characters'), django.core.validators.MaxLengthValidator(22, 'Max value must not contain more than 22 characters')], verbose_name='ЕИО / Имя'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='eio_patronymic',
            field=models.CharField(blank=True, max_length=264, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2, 'Min value should consist of at least 2 characters'), django.core.validators.MaxLengthValidator(22, 'Max value must not contain more than 22 characters')], verbose_name='ЕИО / Отчество'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='eio_surname',
            field=models.CharField(blank=True, max_length=264, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2, 'Min value should consist of at least 2 characters'), django.core.validators.MaxLengthValidator(22, 'Max value must not contain more than 22 characters')], verbose_name='ЕИО / Фамилия'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='inn',
            field=models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(10, 'Min value should consist of at least 10 characters'), django.core.validators.MaxLengthValidator(12, 'Max value must not contain more than 12 characters')], verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='kpp',
            field=models.CharField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(9, 'Min value should consist of at least 9 characters'), django.core.validators.MaxLengthValidator(9, 'Max value must not contain more than 9 characters')], verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=30, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(11, 'Min value should consist of at least 11 characters'), django.core.validators.MaxLengthValidator(11, 'Max value must not contain more than 11 characters')], verbose_name='Телефон'),
        ),
    ]