# Generated by Django 3.1 on 2021-08-23 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0025_auto_20210823_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='status', to='order.orderstatus', verbose_name='Статус'),
        ),
    ]
