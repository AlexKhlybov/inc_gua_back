# Generated by Django 3.1 on 2021-08-12 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_accountingform_accountingformdetail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountingformdetail',
            options={'verbose_name': 'Детальная бухгалтерская форма', 'verbose_name_plural': 'Детальные бухгалтерские формы'},
        ),
    ]
