# Generated by Django 3.1 on 2021-08-23 17:05

import app.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_bankguarantee_bankсontract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bik',
            field=models.CharField(blank=True, max_length=264, validators=[app.validators.check_value_is_digit], verbose_name='БИК'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='correspondent_account_cb',
            field=models.CharField(blank=True, max_length=264, validators=[app.validators.check_value_is_digit], verbose_name='Корреспондентский счет в ЦБ'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='inn',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[app.validators.check_value_is_digit, django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)], verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='kpp',
            field=models.CharField(blank=True, max_length=264, validators=[app.validators.check_value_is_digit], verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='license_number',
            field=models.CharField(blank=True, max_length=264, validators=[app.validators.check_value_is_digit], verbose_name='Номер лицензии'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=30, validators=[app.validators.check_value_is_digit, django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11)], verbose_name='Телефон'),
        ),
    ]
