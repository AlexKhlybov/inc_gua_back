# Generated by Django 3.1 on 2021-08-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_auto_20210708_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='bik',
            field=models.CharField(blank=True, max_length=264, verbose_name='БИК'),
        ),
        migrations.AddField(
            model_name='bank',
            name='contact_patronymic',
            field=models.CharField(blank=True, max_length=264, verbose_name='Контактное лицо / Отчество'),
        ),
        migrations.AddField(
            model_name='bank',
            name='contact_person_name',
            field=models.CharField(blank=True, max_length=264, verbose_name='Контактное лицо / Имя'),
        ),
        migrations.AddField(
            model_name='bank',
            name='contact_person_surname',
            field=models.CharField(blank=True, max_length=264, verbose_name='Контактное лицо / Фамилия'),
        ),
        migrations.AddField(
            model_name='bank',
            name='correspondent_account_cb',
            field=models.CharField(blank=True, max_length=264, verbose_name='Корреспондентский счет в ЦБ'),
        ),
        migrations.AddField(
            model_name='bank',
            name='eio_appointment_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата назначения ЕИО'),
        ),
        migrations.AddField(
            model_name='bank',
            name='eio_name',
            field=models.CharField(blank=True, max_length=264, verbose_name='ЕИО / Имя'),
        ),
        migrations.AddField(
            model_name='bank',
            name='eio_patronymic',
            field=models.CharField(blank=True, max_length=264, verbose_name='ЕИО / Отчество'),
        ),
        migrations.AddField(
            model_name='bank',
            name='eio_surname',
            field=models.CharField(blank=True, max_length=264, verbose_name='ЕИО / Фамилия'),
        ),
        migrations.AddField(
            model_name='bank',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Эл. почта'),
        ),
        migrations.AddField(
            model_name='bank',
            name='inn',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='ИНН'),
        ),
        migrations.AddField(
            model_name='bank',
            name='kpp',
            field=models.CharField(blank=True, max_length=264, verbose_name='КПП'),
        ),
        migrations.AddField(
            model_name='bank',
            name='license_number',
            field=models.CharField(blank=True, max_length=264, verbose_name='Номер лицензии'),
        ),
        migrations.AddField(
            model_name='bank',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='bank',
            name='region',
            field=models.CharField(blank=True, max_length=264, verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='bank',
            name='registration_address',
            field=models.CharField(blank=True, max_length=264, verbose_name='Адрес регистрации'),
        ),
        migrations.AddField(
            model_name='bank',
            name='registration_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата регистрации'),
        ),
    ]
