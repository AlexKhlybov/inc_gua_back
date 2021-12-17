# Generated by Django 3.1 on 2021-08-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0026_auto_20210823_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=1000, verbose_name='Номер лота')),
            ],
            options={
                'verbose_name': 'Лот',
                'verbose_name_plural': 'Лоты',
            },
        ),
    ]
