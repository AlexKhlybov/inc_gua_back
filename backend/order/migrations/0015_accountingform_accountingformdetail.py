# Generated by Django 3.1 on 2021-08-12 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20210809_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingFormDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100, verbose_name='Код строки')),
                ('line_name', models.CharField(blank=True, max_length=300, verbose_name='Название строки')),
                ('start_value', models.IntegerField(blank=True, verbose_name='Значение на начало периода')),
                ('end_value', models.IntegerField(blank=True, verbose_name='Значение на конец периода')),
            ],
            options={
                'verbose_name': 'Бухгалтерская форма',
                'verbose_name_plural': 'Бухгалтерские формы',
            },
        ),
        migrations.CreateModel(
            name='AccountingForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=100, verbose_name='Год')),
                ('organization_type', models.CharField(blank=True, max_length=100, verbose_name='Тип организации')),
                ('detail_form', models.ManyToManyField(blank=True, related_name='detail_form', to='order.AccountingFormDetail', verbose_name='Массив объектов формы')),
            ],
            options={
                'verbose_name': 'Бухгалтерская форма',
                'verbose_name_plural': 'Бухгалтерские формы',
            },
        ),
    ]
