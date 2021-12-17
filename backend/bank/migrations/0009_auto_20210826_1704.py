# Generated by Django 3.1 on 2021-08-26 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_auto_20210824_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankGuaranteeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, verbose_name='Статус банковской гарантии')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Статус банковской гарантии',
                'verbose_name_plural': 'Статусы бансковской гарантии',
            },
        ),
        migrations.AddField(
            model_name='bankguarantee',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='status', to='bank.bankguaranteestatus', verbose_name='Статус'),
        ),
    ]