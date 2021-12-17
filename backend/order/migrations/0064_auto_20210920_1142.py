# Generated by Django 3.1 on 2021-09-20 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('limit', '0009_fzlimits'),
        ('order', '0063_auto_20210917_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='fz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fz_contest', to='limit.limitfz', verbose_name='ФЗ'),
        ),
    ]
