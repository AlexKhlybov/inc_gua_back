# Generated by Django 3.1 on 2021-08-11 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_page', '0001_initial'),
        ('user', '0012_auto_20210811_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangePassword',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Страница смены пароля',
                'verbose_name_plural': 'Страница смены пароля',
            },
            bases=('garpix_page.basepage',),
        ),
    ]