# Generated by Django 3.1 on 2021-07-07 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garpix_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDocumentsPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка заявки (документы)',
                'verbose_name_plural': 'Карточка заявки (документы)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='OrderFinancialReportPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка заявки (финансовая отчетность)',
                'verbose_name_plural': 'Карточка заявки (финансовая отчетность)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='OrderHistoryPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка заявки (история)',
                'verbose_name_plural': 'Карточка заявки (история)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='OrderLimitPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка заявки (лимит)',
                'verbose_name_plural': 'Карточка заявки (лимит)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='OrderPurchasePage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка заявки (закупка)',
                'verbose_name_plural': 'Карточка заявки (закупка)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='OrderQuotationPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка заявки (котировки)',
                'verbose_name_plural': 'Карточка заявки (котировки)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='OrderQuotationTradePage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка заявки (котировки) торг',
                'verbose_name_plural': 'Карточка заявки (котировки) торг',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='OrderRatePage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка заявки (рейтинг)',
                'verbose_name_plural': 'Карточка заявки (рейтинг)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='OrderScoringPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка заявки (скоринг)',
                'verbose_name_plural': 'Карточка заявки (скоринг)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='OrdersPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Заявки',
                'verbose_name_plural': 'Заявки',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='OrderStopFactorsPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка заявки (стоп-факторы и предсигналы)',
                'verbose_name_plural': 'Карточка заявки (стоп-факторы и предсигналы)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='OrderUnderwritingPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Карточка заявки (андеррайтинг)',
                'verbose_name_plural': 'Карточка заявки (андеррайтинг)',
            },
            bases=('garpix_page.basepage',),
        ),
    ]
