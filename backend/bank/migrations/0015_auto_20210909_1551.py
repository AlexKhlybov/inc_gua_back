# Generated by Django 3.1 on 2021-09-09 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0014_auto_20210908_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankguarantee',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='bankguarantee',
            name='date',
        ),
        migrations.RemoveField(
            model_name='bankguarantee',
            name='disclosure_conditions',
        ),
        migrations.RemoveField(
            model_name='bankguarantee',
            name='maintain_a_guarantee',
        ),
        migrations.RemoveField(
            model_name='bankguarantee',
            name='number',
        ),
        migrations.RemoveField(
            model_name='bankguarantee',
            name='rights_and_liabilities_of_the_parties',
        ),
        migrations.RemoveField(
            model_name='bankguarantee',
            name='status',
        ),
        migrations.RemoveField(
            model_name='bankguarantee',
            name='sum',
        ),
        migrations.RemoveField(
            model_name='bankguarantee',
            name='termination_of_liabilities',
        ),
    ]