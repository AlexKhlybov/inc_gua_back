# Generated by Django 3.1 on 2021-09-20 08:42

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('limit', '0008_auto_20210909_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='FZLimits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменено')),
                ('total_limit', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=32, verbose_name='Установленный лимит')),
                ('current_guaranties_sum', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=32, verbose_name='Действующие БГ')),
                ('orders_sum', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=32, verbose_name='Общая сумма заявок')),
                ('free_balance', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=32, verbose_name='Свободный остаток')),
                ('fz', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fz_limits', to='limit.limitfz', verbose_name='ФЗ')),
            ],
            options={
                'verbose_name': 'Лимит ФЗ',
                'verbose_name_plural': 'Лимиты ФЗ',
            },
        ),
    ]
