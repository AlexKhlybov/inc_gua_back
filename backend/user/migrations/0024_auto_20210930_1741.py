# Generated by Django 3.1 on 2021-09-30 14:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20210913_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2, 'Min value should consist of at least 2 characters'), django.core.validators.MaxLengthValidator(22, 'Max value must not contain more than 22 characters')], verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2, 'Min value should consist of at least 2 characters'), django.core.validators.MaxLengthValidator(22, 'Max value must not contain more than 22 characters')], verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ-]*$', 'Cпециальные символы не допускаются, за исключением "-"'), django.core.validators.MinLengthValidator(2, 'Min value should consist of at least 2 characters'), django.core.validators.MaxLengthValidator(22, 'Max value must not contain more than 22 characters')], verbose_name='Отчество'),
        ),
    ]
