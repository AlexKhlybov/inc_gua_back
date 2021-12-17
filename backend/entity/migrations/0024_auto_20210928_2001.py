# Generated by Django 3.1 on 2021-09-28 17:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0023_auto_20210928_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalentity',
            name='okved',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^([\\s\\.]?[0-9]+)+$'), django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(8)], verbose_name='ОКВЭД (Основные)'),
        ),
    ]