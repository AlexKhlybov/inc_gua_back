# Generated by Django 3.1 on 2021-09-10 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0050_auto_20210909_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип Документа',
                'verbose_name_plural': 'Типы Документа',
            },
        ),
        migrations.AlterField(
            model_name='orderdocument',
            name='document_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_document_type', to='order.documenttype', verbose_name='Тип документа'),
        ),
    ]
