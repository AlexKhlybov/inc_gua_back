# Generated by Django 3.1 on 2021-10-18 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0021_document_section'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='bank',
            new_name='document',
        ),
    ]