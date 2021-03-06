# Generated by Django 3.1 on 2021-09-14 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0055_auto_20210913_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderFactors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменено')),
                ('value', models.BooleanField(default=False, verbose_name='Значение')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='order_factors', to='order.order', verbose_name='Заявка')),
                ('sf', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='sf_factors', to='order.sf', verbose_name='СФ')),
            ],
            options={
                'verbose_name': 'Фактор',
                'verbose_name_plural': 'Факторы',
            },
        ),
    ]
