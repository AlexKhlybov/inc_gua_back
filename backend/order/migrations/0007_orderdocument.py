# Generated by Django 3.1 on 2021-07-09 12:45

from django.db import migrations, models
import django.db.models.deletion
import garpix_page.utils.get_file_path


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(default='', upload_to=garpix_page.utils.get_file_path.get_file_path, verbose_name='Документ')),
                ('document_title', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Название документа')),
                ('document_type', models.CharField(choices=[('right', 'Правоустанавливающие документы'), ('financial', 'Финансовые документы'), ('deal', 'Сделка'), ('other', 'Другие документы')], default='other', max_length=64, verbose_name='Тип документа')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='order_documents', to='order.order', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Документ заявки',
                'verbose_name_plural': 'Документы заявки',
            },
        ),
    ]
