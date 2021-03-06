# Generated by Django 3.1 on 2021-09-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0049_auto_20210909_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='guaranty',
            name='guarantee_type',
            field=models.CharField(blank=True, choices=[('Аванс', 'Аванс'), ('На участие в тендере', 'На участие в тендере'), ('На исполнение контракта', 'На исполнение контракта')], default='Аванс', max_length=100, verbose_name='Тип гарантии'),
        ),
        migrations.AddField(
            model_name='order',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AddField(
            model_name='order',
            name='guarantee_type',
            field=models.CharField(blank=True, choices=[('Аванс', 'Аванс'), ('На участие в тендере', 'На участие в тендере'), ('На исполнение контракта', 'На исполнение контракта')], default='Аванс', max_length=100, verbose_name='Тип гарантии'),
        ),
    ]
