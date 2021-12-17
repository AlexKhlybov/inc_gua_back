# Generated by Django 3.1 on 2021-08-16 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_accountingform_principal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountingformdetail',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Код строки'),
        ),
        migrations.AlterField(
            model_name='accountingformdetail',
            name='end_value',
            field=models.IntegerField(blank=True, null=True, verbose_name='Значение на конец периода'),
        ),
        migrations.AlterField(
            model_name='accountingformdetail',
            name='line_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Название строки'),
        ),
        migrations.AlterField(
            model_name='accountingformdetail',
            name='start_value',
            field=models.IntegerField(blank=True, null=True, verbose_name='Значение на начало периода'),
        ),
    ]