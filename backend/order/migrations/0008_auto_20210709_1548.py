# Generated by Django 3.1 on 2021-07-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_orderdocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Комментарий'),
        ),
    ]
