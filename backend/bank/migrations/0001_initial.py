# Generated by Django 3.1 on 2021-07-07 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garpix_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDocumentsPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка банка (документы)',
                'verbose_name_plural': 'Карточка банка (документы)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='BankLimitPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка банка (лимит)',
                'verbose_name_plural': 'Карточка банка (лимит)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='BanksPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Банки',
                'verbose_name_plural': 'Банки',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='BankTariffsPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка банка (тарифы)',
                'verbose_name_plural': 'Карточка банка (тарифы)',
            },
            bases=('garpix_page.basepage',),
        ),
    ]
