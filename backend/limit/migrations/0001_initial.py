# Generated by Django 3.1 on 2021-07-07 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garpix_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LimitBankPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Лимиты (Банк)',
                'verbose_name_plural': 'Лимиты (Банк)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='LimitListPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Лимиты (Список)',
                'verbose_name_plural': 'Лимиты (Список)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='LimitPrincipalPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Лимиты (Принципал)',
                'verbose_name_plural': 'Лимиты (Принципал)',
            },
            bases=('garpix_page.basepage',),
        ),
        migrations.CreateModel(
            name='LimitTypePage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Лимиты (Вид)',
                'verbose_name_plural': 'Лимиты (Вид)',
            },
            bases=('garpix_page.basepage',),
        ),
    ]
