# Generated by Django 3.1 on 2021-07-09 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_beneficiary_principal'),
        ('order', '0005_contract_guaranty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=3, null=True, verbose_name='Рейтинг')),
                ('scoring_ow', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True, verbose_name='Скоринг OW')),
                ('is_stop_factors_exists', models.BooleanField(default=True, verbose_name='Стоп-факторы')),
                ('is_warning_signals_exists', models.BooleanField(default=True, verbose_name='Предсигналы')),
                ('limit_availability_for_region', models.BooleanField(default=True, verbose_name='Доступность лимита на регион')),
                ('limit_availability_for_fz', models.BooleanField(default=True, verbose_name='Доступность лимита на ФЗ')),
                ('limit_availability_for_branch', models.BooleanField(default=True, verbose_name='Доступность лимита на отрасль')),
                ('comment', models.TextField(default='', verbose_name='Комментарий')),
                ('beneficiary', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='beneficiary_orders', to='entity.beneficiary', verbose_name='Бенефициар')),
                ('contract', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='order', to='order.contract', verbose_name='Контракт')),
                ('guaranty', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='order', to='order.guaranty', verbose_name='Гарантия')),
                ('principal', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='principal_orders', to='entity.principal', verbose_name='Принципал')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
