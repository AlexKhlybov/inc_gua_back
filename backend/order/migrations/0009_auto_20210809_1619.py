# Generated by Django 3.1 on 2021-08-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20210709_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='guaranty',
            name='direct_write_off',
            field=models.BooleanField(blank=True, default=False, verbose_name='Прямое списание'),
        ),
        migrations.AddField(
            model_name='guaranty',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время конца'),
        ),
        migrations.AddField(
            model_name='guaranty',
            name='guaranty_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время гарантии'),
        ),
        migrations.AddField(
            model_name='guaranty',
            name='provision',
            field=models.BooleanField(blank=True, default=False, verbose_name='Обеспечение'),
        ),
        migrations.AddField(
            model_name='guaranty',
            name='provision_form',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Форма обеспечения'),
        ),
        migrations.AddField(
            model_name='guaranty',
            name='provision_sum',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сумма обеспечения'),
        ),
        migrations.AddField(
            model_name='guaranty',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время начала'),
        ),
        migrations.AddField(
            model_name='guaranty',
            name='sum',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сумма'),
        ),
        migrations.AddField(
            model_name='guaranty',
            name='take_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время получения'),
        ),
    ]
