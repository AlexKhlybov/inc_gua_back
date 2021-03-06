# Generated by Django 3.1 on 2021-08-26 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0038_fp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='contest',
        ),
        migrations.RemoveField(
            model_name='order',
            name='contract',
        ),
        migrations.AddField(
            model_name='contest',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.contract', verbose_name='Контракт'),
        ),
        migrations.AddField(
            model_name='order',
            name='contest',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='contest_order', to='order.contest', verbose_name='Конкурс'),
        ),
        migrations.AddField(
            model_name='order',
            name='fp',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='fp_order', to='order.fp', verbose_name='ФП'),
        ),
        migrations.AddField(
            model_name='order',
            name='ps',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='ps_order', to='order.ps', verbose_name='ПС'),
        ),
        migrations.AddField(
            model_name='order',
            name='sf',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='sf_order', to='order.sf', verbose_name='СФ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='guaranty',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='guaranty_order', to='order.guaranty', verbose_name='Гарантия'),
        ),
    ]
