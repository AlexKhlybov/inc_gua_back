# Generated by Django 3.1 on 2021-08-04 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0004_auto_20210804_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='inn',
            field=models.CharField(max_length=10, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='inn',
            field=models.CharField(max_length=10, verbose_name='ИНН'),
        ),
    ]
