# Generated by Django 3.1 on 2021-09-13 11:20

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0018_auto_20210908_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменено')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('fraction', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=100, verbose_name='Значение доли')),
            ],
            options={
                'verbose_name': 'Совладелец',
                'verbose_name_plural': 'Совладельцы',
            },
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменено')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('fraction', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=100, verbose_name='Доля')),
                ('co_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownership_co_owner', to='entity.coowner', verbose_name='Совладелец')),
                ('principal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownership_principal', to='entity.principal', verbose_name='Принципал')),
            ],
            options={
                'verbose_name': 'Доля владения',
                'verbose_name_plural': 'Доля владения',
            },
        ),
    ]
