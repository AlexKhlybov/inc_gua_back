# Generated by Django 3.1 on 2021-09-07 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0046_merge_20210831_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderstatus',
            name='description',
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='title',
            field=models.CharField(choices=[('Создана', 'Создана'), ('Отправлена', 'Отправлена'), ('Андеррайтинг новая заявка', 'Андеррайтинг новая заявка'), ('Андеррайтинг в работе', 'Андеррайтинг в работе'), ('Андеррайтинг дозапрос', 'Андеррайтинг дозапрос'), ('Андеррайтинг отказ', 'Андеррайтинг отказ'), ('Котировка авто', 'Котировка авто'), ('Котировка торг', 'Котировка торг'), ('Котировка индивид', 'Котировка индивид'), ('Котировка направлена', 'Котировка направлена'), ('Котировка переопределена', 'Котировка переопределена'), ('Котировка отказ', 'Котировка отказ'), ('Котировка согласована', 'Котировка согласована'), ('Документы дозапрос', 'Документы дозапрос'), ('Документы подпись', 'Документы подпись'), ('Документы отказ', 'Документы отказ'), ('Выпуск гарантии запрошен', 'Выпуск гарантии запрошен'), ('Гарантия выпущена ожидается оплата', 'Гарантия выпущена ожидается оплата'), ('Выпуск гарантии отказ', 'Выпуск гарантии отказ'), ('Гарантия действующая', 'Гарантия действующая'), ('Гарантия получено требование бенефицара', 'Гарантия получено требование бенефицара'), ('Гарантия просрочка уплаты комиссии', 'Гарантия просрочка уплаты комиссии'), ('Гарантия произведена выплата бенефициару', 'Гарантия произведена выплата бенефициару'), ('Гарантия предъявлено регрессное требование к принципалу', 'Гарантия предъявлено регрессное требование принципалу'), ('Гарантия предъявлено требование на выплату страхового возмещения', 'Гарантия предъявлено требование на выплату страхового возмещения'), ('Гарантия истек срок действия', 'Гарантия истек срок действия'), ('Гарантия произведена выплата страхового возмещения', 'Гарантия произведена выплата страхового возмещения'), ('Гарантия прекращена', 'Гарантия прекращена')], default='Создана', max_length=100, verbose_name='Название'),
        ),
    ]
