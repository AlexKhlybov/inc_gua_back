# Generated by Django 3.1 on 2021-08-31 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0016_auto_20210824_1405'),
        ('order', '0044_auto_20210831_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='beneficiary',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='beneficiary_orders', to='entity.beneficiary', verbose_name='Бенефициар'),
        ),
        migrations.AlterField(
            model_name='order',
            name='principal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='principal_orders', to='entity.principal', verbose_name='Принципал'),
        ),
    ]
