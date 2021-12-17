# Generated by Django 3.1 on 2021-08-19 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0023_order_in_archive'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, verbose_name='Статус')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
    ]