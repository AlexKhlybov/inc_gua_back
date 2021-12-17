# Generated by Django 3.1 on 2021-08-23 17:05

import app.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20210811_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, validators=[app.validators.check_value_is_alpha, django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(22)], verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, validators=[app.validators.check_value_is_alpha, django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(22)], verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, validators=[app.validators.check_value_is_alpha, django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(22)], verbose_name='Отчество'),
        ),
    ]
