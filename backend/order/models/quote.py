from datetime import datetime
from decimal import Decimal

from django.db import models

from app.mixins import Timestamps


class Quote(Timestamps):
    class QUOTETYPE:
        AUTO = 'Авто'
        AUCTION = 'Торг'
        INDIVIDUAL = 'Индивидуальная'
        TYPES = (
            (AUTO, 'Авто'),
            (AUCTION, 'Торг'),
            (INDIVIDUAL, 'Индивидуальная'),
        )

    class STATUS:
        PRIMARY = 'Первичная'
        AUTO = 'Авто'
        AUCTION = 'Торг'
        INDIVIDUAL = 'Индивидуальная'
        AGREED = 'Согласована'
        EXPIRED = 'Истек срок действия'
        REFUSAL = 'Отказ'

        TYPES = (
            (PRIMARY, 'Первичная'),
            (AUTO, 'Авто'),
            (AUCTION, 'Торг'),
            (INDIVIDUAL, 'Индивидуальная'),
            (AGREED, 'Согласована'),
            (EXPIRED, 'Истек срок действия'),
            (REFUSAL, 'Отказ'),
        )

    auction = models.ForeignKey('Auction', on_delete=models.CASCADE, related_name='quote_auction', verbose_name='Торг',
                                blank=True, null=True, default=None)
    bank = models.ForeignKey('bank.Bank', on_delete=models.CASCADE, related_name='quote_bank', verbose_name='Банк',
                             blank=True, null=True, default=None)

    guarantee_rate = models.DecimalField('Ставка комиссии по гарантии, % годовых', max_digits=100,
                                         decimal_places=2, default=Decimal('0.00'), blank=True)
    guarantee_sum = models.DecimalField('Сумма гарантии, руб.', max_digits=32, decimal_places=2,
                                        default=Decimal('0.00'), blank=True)
    total_commission = models.DecimalField('Сумма комиссии по гарантии, руб.', max_digits=32, decimal_places=2,
                                           default=Decimal('0.00'), blank=True)
    bank_rate = models.DecimalField('Ставка комиссии банка, % годовых', max_digits=100, decimal_places=2,
                                    default=Decimal('0.00'), blank=True)
    bank_sum = models.DecimalField('Сумма комиссии банка, руб.', max_digits=32, decimal_places=2,
                                   default=Decimal('0.00'), blank=True)
    bank_commission = models.DecimalField('Доля в комиссии по гарантии, %', max_digits=100, decimal_places=2,
                                          default=Decimal('0.00'), blank=True)
    insurance_premium_rate = models.DecimalField('Ставка страховой премии', max_digits=100, decimal_places=2,
                                                 default=Decimal('0.00'), blank=True)
    insurance_premium_sum = models.DecimalField('Сумма страховой премии', max_digits=32, decimal_places=2,
                                                default=Decimal('0.00'), blank=True)
    insurance_premium_commission = models.DecimalField('Доля в комиссии по гарантии, %', max_digits=100,
                                                       decimal_places=2, default=Decimal('0.00'), blank=True)
    master_agent_rate = models.DecimalField('Ставка комиссии мастер-агента, % годовых', max_digits=100,
                                            decimal_places=2, default=Decimal('0.00'), blank=True)
    master_agent_sum = models.DecimalField('Сумма комиссии мастер-агента, руб.', max_digits=32,
                                           decimal_places=2, default=Decimal('0.00'), blank=True)
    master_agent_commission = models.DecimalField('Доля в комиссии по гарантии, %', max_digits=100,
                                                  decimal_places=2, default=Decimal('0.00'), blank=True)
    agent_rate = models.DecimalField('Ставка комиссии агента, % годовых', max_digits=100,
                                     decimal_places=2, default=Decimal('0.00'), blank=True)
    agent_sum = models.DecimalField('Сумма комиссии агента, руб.', max_digits=32,
                                    decimal_places=2, default=Decimal('0.00'), blank=True)
    agent_commission = models.DecimalField('Доля в комиссии по гарантии, %', max_digits=100,
                                           decimal_places=2, default=Decimal('0.00'), blank=True)

    type = models.CharField('Вид котировки', max_length=128, choices=QUOTETYPE.TYPES, default=QUOTETYPE.TYPES[0])
    status = models.CharField('Статус котировки', max_length=128, choices=STATUS.TYPES, default=STATUS.TYPES[0])

    expiry_date = models.DateField(verbose_name='Действует до')
    is_edited = models.BooleanField(verbose_name='Заблокирован', default=False)

    @property
    def is_expired(self):
        if datetime.now > self.expiry_date:
            return True
        return False

    class Meta:
        verbose_name = 'Котировка'
        verbose_name_plural = 'Котировки'

    def __str__(self):
        return f'Котировка: {self.type}({self.status}) - {self.auction} - {self.bank}'

    def save(self, *args, **kwargs):
        total_sum = self.bank_sum + self.insurance_premium_sum + self.master_agent_sum + self.agent_sum
        if total_sum == 0:
            self.bank_sum = self.insurance_premium_sum = self.master_agent_sum = self.agent_sum = 0
        else:
            self.bank_commission = self.bank_sum / total_sum * 100
            self.insurance_premium_commission = self.insurance_premium_sum / total_sum * 100
            self.master_agent_commission = self.master_agent_sum / total_sum * 100
            self.agent_commission = self.agent_sum / total_sum * 100
        self.total_commission = total_sum
        super(Quote, self).save(*args, **kwargs)
