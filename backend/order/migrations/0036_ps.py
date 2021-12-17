# Generated by Django 3.1 on 2021-08-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0035_auto_20210826_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, verbose_name='Название')),
                ('value', models.BooleanField(default=False, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Пс',
                'verbose_name_plural': 'Пс',
            },
        ),
    ]