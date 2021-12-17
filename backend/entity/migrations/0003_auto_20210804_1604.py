# Generated by Django 3.1 on 2021-08-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_beneficiary_principal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='inn',
            field=models.IntegerField(max_length=10, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='region',
            field=models.CharField(max_length=128, verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='inn',
            field=models.IntegerField(max_length=10, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='region',
            field=models.CharField(max_length=128, verbose_name='Регион'),
        ),
    ]
