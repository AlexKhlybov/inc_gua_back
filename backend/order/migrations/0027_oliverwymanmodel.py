# Generated by Django 3.1 on 2021-08-25 12:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0016_auto_20210824_1405'),
        ('order', '0026_auto_20210823_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='OliverWymanModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplierInn', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)], verbose_name='ИНН исполнителя')),
                ('customerInn', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры'), django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)], verbose_name='ИНН заказчика')),
                ('reportType', models.CharField(choices=[('Y', 'Y'), ('Q', 'Q')], default='Y', max_length=2, verbose_name='Тип отчета')),
                ('signals_BS_1', models.BooleanField(default=False, verbose_name='Наличие задолженности по упате налогов')),
                ('signals_BS_2', models.BooleanField(default=False, verbose_name='Отсутствие по юр. адресу')),
                ('signals_BS_5', models.BooleanField(default=False, verbose_name='Входит на данный момент в реестр недобросовестных поставщиков')),
                ('signals_BS_6', models.BooleanField(default=False, verbose_name='Ранее входил в реестр недобросовестных поставщиков')),
                ('signals_BS_7', models.BooleanField(default=False, verbose_name='Не предоставляние налоговой отчетности более года ')),
                ('signals_BS_10', models.BooleanField(default=False, verbose_name='Наличие активных дел по банкротству в отношении компании')),
                ('signals_BS_14', models.BooleanField(default=False, verbose_name='Наличие исполнительных производств по заработной плате за последний год')),
                ('signals_BS_15', models.BooleanField(default=False, verbose_name='Наличие исполнительных производств с арестом на сумму более 100 тыс. руб.')),
                ('signals_BS_16', models.BooleanField(default=False, verbose_name='Вхождение в реестр дисквалифицированных лиц')),
                ('signals_BS_18', models.BooleanField(default=False, verbose_name='Наличие флага банкротства')),
                ('signals_BS_22', models.BooleanField(default=False, verbose_name='Отношение суммы закупки к выручке больше 1.5')),
                ('signals_BS_23', models.BooleanField(default=False, verbose_name='Ранее были раскрытые гарантии')),
                ('signals_BS_111', models.BooleanField(default=False, verbose_name='Наличие активных судов против текущего заказчика в качестве ответчика')),
                ('signals_GS_0', models.BooleanField(default=False, verbose_name='Выручка больше 1 млрд.')),
                ('courts_1', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=32, null=True, verbose_name='Количество судебных дел в качестве ответчика за последние 2 года ')),
                ('courts_2', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=32, null=True, verbose_name='Средняя длительность судебного дела за последние 2 года')),
                ('courts_3', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=32, null=True, verbose_name='Количество судебных дел в качестве истца за последние 2 года')),
                ('courts_4', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=32, null=True, verbose_name='Общая сумма судов в качестве ответчика за последний год / Чистая прибыль')),
                ('courts_5', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=32, null=True, verbose_name='Общая сумма судов в качестве ответчика за последний год / EBITDA')),
                ('executory_1', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=32, null=True, verbose_name='Количество исполнительных производств по значимым делам за последние 2 года')),
                ('executory_2', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=32, null=True, verbose_name='Сумма исполнительных производств за последний год / Чистая прибыль')),
                ('tenders_1', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=32, null=True, verbose_name='Количество тендеров за последний год')),
                ('tenders_2', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=32, null=True, verbose_name='Количество выигранных тендеров с данным заказчиком за последние 5 лет')),
                ('tenders_3', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=32, null=True, verbose_name='Доля выигранных тендеров Принципалом за последние 2 года ')),
                ('tenders_4', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=32, null=True, verbose_name='Отношение общей суммы тендерных закупок за прошлый год к выручке')),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='customer', to='entity.beneficiary', verbose_name='Заказчик')),
                ('supplier', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='supplier', to='entity.principal', verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name': 'Отчет Oliver Wyman',
                'verbose_name_plural': 'Отчеты Oliver Wyman',
            },
        ),
    ]
