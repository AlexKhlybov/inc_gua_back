# Generated by Django 3.1 on 2021-09-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0061_auto_20210917_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='guarantydocument',
            name='is_valid',
            field=models.BooleanField(default=False, verbose_name='Валидный'),
        ),
        migrations.AddField(
            model_name='orderdocument',
            name='is_valid',
            field=models.BooleanField(default=False, verbose_name='Валидный'),
        ),
    ]
