# Generated by Django 3.1 on 2021-07-12 07:44

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_auto_20210708_1859'),
        ('limit', '0002_auto_20210708_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='LimitBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=32, verbose_name='Лимит')),
                ('bank', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='limit_bank', to='bank.bank', verbose_name='Банк')),
            ],
            options={
                'verbose_name': 'Лимит банка',
                'verbose_name_plural': 'Лимиты банков',
            },
        ),
    ]