# Generated by Django 3.1 on 2021-10-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changelog', '0003_auto_20211005_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changelog',
            name='newvalue',
            field=models.CharField(blank=True, default='', max_length=2000, verbose_name='Текущее значение'),
        ),
        migrations.AlterField(
            model_name='changelog',
            name='oldvalue',
            field=models.CharField(blank=True, default='', max_length=2000, verbose_name='Предыдущее значение'),
        ),
    ]
