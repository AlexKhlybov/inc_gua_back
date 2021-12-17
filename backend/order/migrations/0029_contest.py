# Generated by Django 3.1 on 2021-08-25 12:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0028_contesttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defined', models.BooleanField(default=False, verbose_name='Определен?')),
                ('fz', models.CharField(blank=True, max_length=100, verbose_name='ФЗ')),
                ('okpd2', models.CharField(blank=True, max_length=1000, verbose_name='ОКПД2')),
                ('nmck', models.CharField(blank=True, max_length=1000, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11)], verbose_name='НМЦК')),
                ('lot', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='order.lot', verbose_name='Лот')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.contesttype', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Конкурс',
                'verbose_name_plural': 'Конкурсы',
            },
        ),
    ]
