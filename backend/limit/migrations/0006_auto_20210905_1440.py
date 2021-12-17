# Generated by Django 3.1 on 2021-09-05 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('limit', '0005_auto_20210905_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='limit',
            name='limit_bank',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='limits_bank', to='limit.limitbank', verbose_name='Лимит Банка'),
        ),
        migrations.AlterField(
            model_name='limit',
            name='limit_fz',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='limits_fz', to='limit.limitfz', verbose_name='Лимит ФЗ'),
        ),
        migrations.AlterField(
            model_name='limit',
            name='limit_principal',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='limits_principal', to='limit.limitprincipalmodel', verbose_name='Лимит Принципала'),
        ),
    ]