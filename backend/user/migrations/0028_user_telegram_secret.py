# Generated by Django 3.1 on 2021-10-21 11:12

from django.db import migrations, models
import garpix_notify.mixins.user_notify_mixin


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_user_authority'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram_secret',
            field=models.CharField(default=garpix_notify.mixins.user_notify_mixin.generate_uuid, max_length=150, unique=True, verbose_name='Ключ подключения Telegram'),
        ),
    ]
