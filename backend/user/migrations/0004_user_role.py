# Generated by Django 3.1 on 2021-07-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210708_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('underwriter', 'Андеррайтер'), ('master_underwriter', 'Мастер-андеррайтер'), ('principal', 'Принципал'), ('agent', 'Агент'), ('bank', 'Банк')], max_length=32, null=True, verbose_name='Роль'),
        ),
    ]
