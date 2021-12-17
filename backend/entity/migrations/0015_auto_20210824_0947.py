# Generated by Django 3.1 on 2021-08-24 06:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0014_auto_20210823_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='inn',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'значение должно содержать только цифры'), django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)], verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='department_code',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'значение должно содержать только цифры'), django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(6)], verbose_name='Код подразделения'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator('^[a-zA-Z-]*$', 'cпециальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(22)], verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='inn',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'значение должно содержать только цифры'), django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)], verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator('^[a-zA-Z-]*$', 'cпециальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(22)], verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='passport_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'значение должно содержать только цифры'), django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(6)], verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='passport_series',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'значение должно содержать только цифры'), django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4)], verbose_name='Серия паспорта'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='patronymic',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator('^[a-zA-Z-]*$', 'cпециальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(22)], verbose_name='Отчество'),
        ),
    ]
