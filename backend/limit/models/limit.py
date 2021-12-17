from django.db import models
from decimal import Decimal

from app.mixins import Timestamps
from limit.models import LimitFZ, LimitPrincipalModel, LimitBank
from entity.models import Principal


class Limit(Timestamps):

    CHOICES_RATING = [
        ('Рейтинг', (
            ('A+', 'A+'),
            ('A', 'A'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B', 'B'),
            ('B-', 'B-'),
            ('C+', 'C+'),
            ('C', 'C'),
            ('C-', 'C-'),
            ('D', 'D'),
        ))
    ]
    principal = models.OneToOneField(Principal, on_delete=models.CASCADE, related_name='limits_principal', blank=False,
                                     null=False, verbose_name='Принципал', default=None)
    limit_fz = models.ForeignKey(LimitFZ, on_delete=models.CASCADE, related_name='limits_fz', blank=True,
                                 null=True, verbose_name='Лимит ФЗ', default='')
    limit_bank = models.ForeignKey(LimitBank, on_delete=models.CASCADE, related_name='limits_bank', blank=True,
                                   null=True, verbose_name='Лимит Банка', default='')
    limit_principal = models.ForeignKey(LimitPrincipalModel, on_delete=models.CASCADE, related_name='limits_principal', blank=True,
                                        null=True, verbose_name='Лимит Принципала', default='')
    ball_rating = models.DecimalField(verbose_name='Расчетный рейтинг в баллах', max_digits=3, decimal_places=2, default=Decimal('0.00'))
    ball_rating_total = models.DecimalField(verbose_name='Итоговый рейтинг в баллах', max_digits=3, decimal_places=2,
                                            blank=True, default=Decimal('0.00'))
    letter_rating = models.CharField(verbose_name='Буквенный рейтинг', max_length=32, choices=CHOICES_RATING, blank=True, default='')
    financial_indicators = models.DecimalField(verbose_name='Финансовые показатели', blank=True, max_digits=32,
                                               decimal_places=2, default=Decimal('0.00'))
    work_exp = models.DecimalField(verbose_name='Опыт работы', blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))
    score_big_contracts = models.DecimalField(verbose_name='Количество исполненных за последние 3 года контрактов, стоимостью более '
                                                           'либо равной контракту, по которому требуется гарантия',
                                              max_digits=32, blank=True, decimal_places=2, default=Decimal('0.00'))
    score_all_contracts = models.DecimalField(verbose_name='Количество исполненных контрактов за последние 3 года',
                                              blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))
    score_year = models.DecimalField(verbose_name='Срок работы Принципала в основном направлении деятельности (лет)',
                                     blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))
    additional_factors = models.DecimalField(verbose_name='Дополнительные факторы',
                                             blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))
    ownership_structure = models.DecimalField(verbose_name='Структура владения',
                                              blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))
    delta = models.DecimalField(verbose_name='Мнение UW',
                                blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))

    # доп факторы
    add_factor_1 = models.DecimalField(verbose_name='Наличие существенной по суммам и/или срокам текущей Картотеки неопл. расчетов',
                                       blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))
    add_factor_2 = models.DecimalField(verbose_name='Наличие существенной по суммам и/или срокам задолженности перед фед. бюдж.',
                                       blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))
    add_factor_3 = models.DecimalField(verbose_name='Наличие просроченной задолженности перед работниками по зараб. плате',
                                       blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))
    add_factor_4 = models.DecimalField(verbose_name='Бюджетные активы, неликвидные запасы на последнюю отчетную дату',
                                       blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))
    add_factor_5 = models.DecimalField(verbose_name='Безнадежная дебиторская задолженность на последнюю отчетную дату',
                                       blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))
    add_factor_6 = models.DecimalField(verbose_name='Наличие текущего убытка с учетом что имеется накопленная прибыль',
                                       blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))
    add_factor_7 = models.DecimalField(verbose_name='Текущий убыток при условии что ЧА положительные',
                                       blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))
    add_factor_8 = models.DecimalField(verbose_name='Существенное снижение ЧА',
                                       blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))
    add_factor_9 = models.DecimalField(verbose_name='Участие в судебном(ых) процессе(ах)',
                                       blank=True, max_digits=32, decimal_places=2, default=Decimal('0.00'))

    class Meta:
        verbose_name = 'Лимит'
        verbose_name_plural = 'Лимиты'

    def __str__(self):
        return f'Лимиты принципала - {self.principal}'

    def get_principal_rating(self, total):
        rating_list = {
            9.3: ("A+", 4.5, 50),
            8.6: ("A", 4.0, 50),
            7.9: ("A-", 3.5, 50),
            7.2: ("B+", 3.0, 35),
            6.5: ("B", 2.5, 35),
            5.8: ("B-", 2.0, 35),
            5.1: ("C+", 1.5, 20),
            4.4: ("C", 1.0, 20),
            3.5: ("C-", 0, 0),
            0: ("D", 0, 0),
        }
        for max_n, data in rating_list.items():
            if total >= max_n:
                RATING = {"rating": data[0], "k": data[1], "mdo": data[2]}
                return RATING

    def save(self, *args, **kwargs):
        self.ball_rating_total = min(self.ball_rating - self.additional_factors * Decimal(0.11) + self.delta, 9.9)
        self.letter_rating = self.get_principal_rating(self.ball_rating_total)['rating']
        super(Limit, self).save(*args, **kwargs)
