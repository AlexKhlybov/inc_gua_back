# Generated by Django 3.1 on 2021-08-26 08:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0034_auto_20210825_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guaranty',
            name='direct_write_off',
        ),
        migrations.RemoveField(
            model_name='guaranty',
            name='fz',
        ),
        migrations.RemoveField(
            model_name='guaranty',
            name='guaranty_time',
        ),
        migrations.AddField(
            model_name='guaranty',
            name='availability_without_acceptance',
            field=models.BooleanField(blank=True, default=False, verbose_name='Наличие права безакцептного списание'),
        ),
        migrations.AddField(
            model_name='guaranty',
            name='security_under_guarantee',
            field=models.BooleanField(blank=True, default=False, verbose_name='Обеспечение по гарантии'),
        ),
        migrations.AlterField(
            model_name='guaranty',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата конца действия гарантии'),
        ),
        migrations.AlterField(
            model_name='guaranty',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата начала действия гарантии'),
        ),
        migrations.AlterField(
            model_name='guaranty',
            name='take_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата получения БГ'),
        ),
        migrations.AlterField(
            model_name='guaranty',
            name='term',
            field=models.CharField(blank=True, max_length=1000, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Значение должно содержать только цифры')], verbose_name='Срок гарантии'),
        ),
    ]