# Generated by Django 3.1 on 2021-08-19 14:00

from django.db import migrations, models
import garpix_utils.file.file_field


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0010_auto_20210819_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=garpix_utils.file.file_field.get_file_path, verbose_name='Документ'),
        ),
    ]