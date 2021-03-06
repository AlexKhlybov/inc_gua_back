# Generated by Django 3.1 on 2021-09-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0006_auto_20210720_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='blacklistitem',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано'),
        ),
        migrations.AddField(
            model_name='blacklistitem',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Изменено'),
        ),
        migrations.AddField(
            model_name='stopfactor',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано'),
        ),
        migrations.AddField(
            model_name='stopfactor',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Изменено'),
        ),
        migrations.AddField(
            model_name='warningsignal',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано'),
        ),
        migrations.AddField(
            model_name='warningsignal',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Изменено'),
        ),
    ]
