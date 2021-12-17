from django.db import models

from app.mixins import Timestamps


class OrderStatus(Timestamps):
    class STATUSES:
        CREATED = 'Создана'
        SENT = 'Отправлена'

        UNDERWRITING_A_NEW_APPLICATION = 'Андеррайтинг новая заявка'
        UNDERWRITING_IN_PROGRESS = 'Андеррайтинг в работе'
        UNDERWRITING_REQUERY = 'Андеррайтинг дозапрос'
        UNDERWRITING_REFUSAL = 'Андеррайтинг отказ'

        QUOTE_AUTO = 'Котировка авто'
        QUOTE_AUCTION = 'Котировка торг'
        QUOTE_INDIVIDUAL = 'Котировка индивид'
        QUOTE_SENT = 'Котировка направлена'
        QUOTE_REDEFINED = 'Котировка переопределена'
        QUOTE_REFUSAL = 'Котировка отказ'
        QUOTE_AGREED = 'Котировка согласована'

        DOCUMENTS_REQUERY = 'Документы дозапрос'
        DOCUMENTS_SIGNATURE = 'Документы подпись'
        DOCUMENTS_REFUSAL = 'Документы отказ'

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
            (CREATED, 'Создана'),
            (SENT, 'Отправлена'),

            (UNDERWRITING_A_NEW_APPLICATION, 'Андеррайтинг новая заявка'),
            (UNDERWRITING_IN_PROGRESS, 'Андеррайтинг в работе'),
            (UNDERWRITING_REQUERY, 'Андеррайтинг дозапрос'),
            (UNDERWRITING_REFUSAL, 'Андеррайтинг отказ'),

            (QUOTE_AUTO, 'Котировка авто'),
            (QUOTE_AUCTION, 'Котировка торг'),
            (QUOTE_INDIVIDUAL, 'Котировка индивид'),
            (QUOTE_SENT, 'Котировка направлена'),
            (QUOTE_REDEFINED, 'Котировка переопределена'),
            (QUOTE_REFUSAL, 'Котировка отказ'),
            (QUOTE_AGREED, 'Котировка согласована'),

            (DOCUMENTS_REQUERY, 'Документы дозапрос'),
            (DOCUMENTS_SIGNATURE, 'Документы подпись'),
            (DOCUMENTS_REFUSAL, 'Документы отказ'),

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
    limit_include = models.BooleanField(verbose_name='Учитывать при расчете лимита', default=False)

    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статусы заявки'

    def __str__(self):
        return self.title
