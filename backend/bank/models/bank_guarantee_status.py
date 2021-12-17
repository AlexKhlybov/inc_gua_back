from django.db import models

from app.mixins import Timestamps


class BankGuaranteeStatus(Timestamps):
    class STATUSES:
        WARRANTY_ISSUE_REQUESTED = 'Выпуск гарантии запрошен'
        GUARANTEE_ISSUED_PAYMENT_EXPECTED = 'Гарантия выпущена ожидается оплата'
        WARRANTY_DISCLAIMER = 'Выпуск гарантии отказ'
        WARRANTY_VALID = 'Гарантия действующая'
        GUARANTEE_BENEFICIARY_CLAIM_RECEIVED = 'Гарантия получено требование бенефицара'
        GUARANTEE_LATE_PAYMENT_COMMISSION = 'Гарантия просрочка уплаты комиссии'
        GUARANTEE_PAYMENT_MADE_BENEFICIARY = 'Гарантия произведена выплата бенефициару'
        GUARANTEE_RECOURSE_CLAIM_MADE_AGAINST_PRINCIPAL = 'Гарантия предъявлено регрессное требование к принципалу'
        GUARANTEE_CLAIM_PAYMENT_INSURANCE_COMPENSATION = 'Гарантия предъявлено требование на выплату страхового возмещения'
        WARRANTY_EXPIRED = 'Гарантия истек срок действия'
        GUARANTEE_PAYMENT_INSURANCE_COMPENSATION_MADE = 'Гарантия произведена выплата страхового возмещения'
        WARRANTY_TERMINATED = 'Гарантия прекращена'
        TYPES = (
            (WARRANTY_ISSUE_REQUESTED, 'Выпуск гарантии запрошен'),
            (GUARANTEE_ISSUED_PAYMENT_EXPECTED, 'Гарантия выпущена ожидается оплата'),
            (WARRANTY_DISCLAIMER, 'Выпуск гарантии отказ'),
            (WARRANTY_VALID, 'Гарантия действующая'),
            (GUARANTEE_BENEFICIARY_CLAIM_RECEIVED, 'Гарантия получено требование бенефицара'),
            (GUARANTEE_LATE_PAYMENT_COMMISSION, 'Гарантия просрочка уплаты комиссии'),
            (GUARANTEE_PAYMENT_MADE_BENEFICIARY, 'Гарантия произведена выплата бенефициару'),
            (GUARANTEE_RECOURSE_CLAIM_MADE_AGAINST_PRINCIPAL, 'Гарантия предъявлено регрессное требование принципалу'),
            (GUARANTEE_CLAIM_PAYMENT_INSURANCE_COMPENSATION,
             'Гарантия предъявлено требование на выплату страхового возмещения'),
            (WARRANTY_EXPIRED, 'Гарантия истек срок действия'),
            (GUARANTEE_PAYMENT_INSURANCE_COMPENSATION_MADE, 'Гарантия произведена выплата страхового возмещения'),
            (WARRANTY_TERMINATED, 'Гарантия прекращена'),
        )

    title = models.CharField(max_length=100, verbose_name='Название', choices=STATUSES.TYPES, default='Создана')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='')
    limit_include = models.BooleanField(verbose_name='Учитывать при расчете лимита', default=False)

    class Meta:
        verbose_name = 'Статус банковской гарантии'
        verbose_name_plural = 'Статусы бансковской гарантии'

    def __str__(self):
        return self.title
