# Generated by Django 3.1 on 2021-08-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20210809_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guaranty',
            name='provision_sum',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Сумма обеспечения'),
        ),
        migrations.AlterField(
            model_name='guaranty',
            name='sum',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Сумма'),
        ),
    ]