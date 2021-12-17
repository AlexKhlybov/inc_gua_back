# Generated by Django 3.1 on 2021-08-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_auto_20210812_1909'),
        ('entity', '0006_principal_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='principal',
            name='accounting_forms',
            field=models.ManyToManyField(blank=True, related_name='principal_accounting_forms', to='order.AccountingForm', verbose_name='Бухгалтерские формы'),
        ),
    ]
