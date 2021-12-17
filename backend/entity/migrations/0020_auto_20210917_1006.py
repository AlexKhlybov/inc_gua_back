# Generated by Django 3.1 on 2021-09-17 07:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0019_coowner_ownership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalentity',
            name='bank_inn',
            field=models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(12)], verbose_name='ИНН банка'),
        ),
        migrations.AlterField(
            model_name='legalentity',
            name='inn',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(12)], verbose_name='ИНН'),
        ),
    ]
