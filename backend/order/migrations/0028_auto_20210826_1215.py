# Generated by Django 3.1 on 2021-08-26 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0027_oliverwymanmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='oliverwymanmodel',
            name='courts_6',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=32, null=True, verbose_name='Общая сумма судов в качестве ответчика за последний год / EBITDA'),
        ),
        migrations.AlterField(
            model_name='oliverwymanmodel',
            name='courts_4',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=32, null=True, verbose_name='Общая сумма судов в качестве ответчика за последний год'),
        ),
        migrations.AlterField(
            model_name='oliverwymanmodel',
            name='courts_5',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=32, null=True, verbose_name='Общая сумма судов в качестве ответчика за последний год / Чистая прибыль'),
        ),
        migrations.AlterField(
            model_name='oliverwymanmodel',
            name='executory_1',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=32, null=True, verbose_name='Количество исполнительных производств по значимым делам за последние 2 года'),
        ),
        migrations.AlterField(
            model_name='oliverwymanmodel',
            name='executory_2',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=32, null=True, verbose_name='Сумма исполнительных производств за последний год / Чистая прибыль'),
        ),
        migrations.AlterField(
            model_name='oliverwymanmodel',
            name='tenders_3',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=32, null=True, verbose_name='Доля выигранных тендеров Принципалом за последние 2 года '),
        ),
        migrations.AlterField(
            model_name='oliverwymanmodel',
            name='tenders_4',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=32, null=True, verbose_name='Отношение общей суммы тендерных закупок за прошлый год к выручке'),
        ),
    ]
