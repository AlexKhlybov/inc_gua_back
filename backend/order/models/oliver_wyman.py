from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils.translation import gettext as _

from app.mixins import Timestamps
from entity.models import Beneficiary, Principal


class OliverWymanModel(Timestamps):
    class ORDERTYPE:
        YEAR = 'Y'
        QUARTER = 'Q'
        TYPES = (
            (YEAR, 'Y'),
            (QUARTER, 'Q'),
        )

    supplier = models.ForeignKey(Principal, verbose_name='Исполнитель', blank=False, null=False, default=None,
                                 on_delete=models.SET_DEFAULT, related_name='supplier')
    customer = models.ForeignKey(Beneficiary, verbose_name='Заказчик', blank=False, null=False, default=None,
                                 on_delete=models.SET_DEFAULT, related_name='customer')
    supplierInn = models.CharField(
        max_length=12, verbose_name='ИНН исполнителя', blank=True, null=True,
        validators=[RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                    MinLengthValidator(10, _('Min value should consist of at least 10 characters')),
                    MaxLengthValidator(12, _('Max value must not contain more than 12 characters')), ])
    customerInn = models.CharField(max_length=12, verbose_name='ИНН заказчика', blank=True, null=True,
                                   validators=[RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры'),
                                               MinLengthValidator(10), MaxLengthValidator(12), ])
    reportType = models.CharField(max_length=2, verbose_name='Тип отчета', choices=ORDERTYPE.TYPES,
                                  blank=False, null=False, default=ORDERTYPE.YEAR)
    purchaseNumber = models.CharField(max_length=128, verbose_name='Номер закупки', blank=True, null=True)
    signals_BS_1 = models.BooleanField(verbose_name='Наличие задолженности по упате налогов', default=False)
    signals_BS_2 = models.BooleanField(verbose_name='Отсутствие по юр. адресу', default=False)
    signals_BS_5 = models.BooleanField(verbose_name='Входит на данный момент в реестр недобросовестных поставщиков',
                                       default=False)
    signals_BS_6 = models.BooleanField(verbose_name='Ранее входил в реестр недобросовестных поставщиков', default=False)
    signals_BS_7 = models.BooleanField(verbose_name='Не предоставляние налоговой отчетности более года ', default=False)
    signals_BS_10 = models.BooleanField(verbose_name='Наличие активных дел по банкротству в отношении компании',
                                        default=False)
    signals_BS_14 = models.BooleanField(
        verbose_name='Наличие исполнительных производств по заработной плате за последний год', default=False)
    signals_BS_15 = models.BooleanField(
        verbose_name='Наличие исполнительных производств с арестом на сумму более 100 тыс. руб.', default=False)
    signals_BS_16 = models.BooleanField(verbose_name='Вхождение в реестр дисквалифицированных лиц', default=False)
    signals_BS_18 = models.BooleanField(verbose_name='Наличие флага банкротства', default=False)
    signals_BS_22 = models.BooleanField(verbose_name='Отношение суммы закупки к выручке больше 1.5', default=False)
    signals_BS_23 = models.BooleanField(verbose_name='Ранее были раскрытые гарантии', default=False)
    signals_BS_111 = models.BooleanField(
        verbose_name='Наличие активных судов против текущего заказчика в качестве ответчика', default=False)
    signals_GS_0 = models.BooleanField(verbose_name='Выручка больше 1 млрд.', default=False)

    courts_1 = models.DecimalField(
        verbose_name='Количество судебных дел в качестве ответчика за последние 2 года ', max_digits=32,
        decimal_places=0, blank=True, null=True, default=0)
    courts_2 = models.DecimalField(
        verbose_name='Средняя длительность судебного дела за последние 2 года', max_digits=32,
        decimal_places=0, blank=True, null=True, default=0)
    courts_3 = models.DecimalField(
        verbose_name='Количество судебных дел в качестве истца за последние 2 года', max_digits=32,
        decimal_places=0, blank=True, null=True, default=0)
    courts_4 = models.DecimalField(
        verbose_name='Общая сумма судов в качестве ответчика за последний год', max_digits=32,
        decimal_places=2, blank=True, null=True, default=0.00)
    courts_5 = models.DecimalField(
        verbose_name='Общая сумма судов в качестве ответчика за последний год / Чистая прибыль', max_digits=32,
        decimal_places=2, blank=True, null=True, default=0.00)
    courts_6 = models.DecimalField(
        verbose_name='Общая сумма судов в качестве ответчика за последний год / EBITDA', max_digits=32,
        decimal_places=2, blank=True, null=True, default=0)

    executory_1 = models.DecimalField(
        verbose_name='Количество исполнительных производств по значимым делам за последние 2 года', max_digits=32,
        decimal_places=2, blank=True, null=True, default=0.00)
    executory_2 = models.DecimalField(
        verbose_name='Сумма исполнительных производств за последний год / Чистая прибыль', max_digits=32,
        decimal_places=2, blank=True, null=True, default=0.00)

    tenders_1 = models.DecimalField(
        verbose_name='Количество тендеров за последний год', max_digits=32,
        decimal_places=0, blank=True, null=True, default=0)
    tenders_2 = models.DecimalField(
        verbose_name='Количество выигранных тендеров с данным заказчиком за последние 5 лет', max_digits=32,
        decimal_places=0, blank=True, null=True, default=0)
    tenders_3 = models.DecimalField(
        verbose_name='Доля выигранных тендеров Принципалом за последние 2 года ', max_digits=32,
        decimal_places=2, blank=True, null=True, default=0.00)
    tenders_4 = models.DecimalField(
        verbose_name='Отношение общей суммы тендерных закупок за прошлый год к выручке', max_digits=32,
        decimal_places=2, blank=True, null=True, default=0.00)

    finance_module = models.DecimalField(
        verbose_name='Балл финансового модуля', max_digits=32, decimal_places=2, blank=True, null=True, default=0.00)
    qualitative_module = models.DecimalField(
        verbose_name='Балл качественного модуля', max_digits=32, decimal_places=2, blank=True, null=True, default=0.00)
    tenders_module = models.DecimalField(
        verbose_name='Балл модуля тендеров', max_digits=32, decimal_places=2, blank=True, null=True, default=0.00)
    courts_module = models.DecimalField(
        verbose_name='Балл модуля арбитражных судов', max_digits=32, decimal_places=2, blank=True, null=True,
        default=0.00)
    executory_module = models.DecimalField(
        verbose_name='Балл модуля исполнительных производств', max_digits=32, decimal_places=2, blank=True, null=True,
        default=0.00)
    signals_module = models.DecimalField(
        verbose_name='Балл модуля сигналов', max_digits=32, decimal_places=2, blank=True, null=True, default=0.00)
    pd_pit = models.DecimalField(
        verbose_name='Вероятность раскрытия гарантии (в долях)', max_digits=32, decimal_places=2, blank=True, null=True,
        default=0.00)
    pd_ttc = models.DecimalField(
        verbose_name='Вероятность раскрытия гарантии (TTC)', max_digits=32, decimal_places=2, blank=True, null=True,
        default=0.00)

    capital_assets = models.DecimalField(verbose_name='Капитал/Активы', max_digits=32, decimal_places=2, blank=True,
                                         null=True, default=0.00)
    dynamics_of_revenue_year_to_year = models.DecimalField(verbose_name='Выручка/Выручка(пред. год)', max_digits=32,
                                                           decimal_places=2, blank=True, null=True, default=0.00)
    EBITDA_short_term_debt_cash_and_interest_payments = models.DecimalField(
        verbose_name='Отношение EBITDA к кредиторской задолженности',
        max_digits=32, decimal_places=2, blank=True, null=True, default=0.00)
    EBITDA_total_liabilities = models.DecimalField(verbose_name='EBITDA / Общие обязательства', max_digits=32,
                                                   decimal_places=2, blank=True, null=True, default=0.00)
    instant_liquidity = models.DecimalField(verbose_name='Мгновенная ликвидность', max_digits=32, decimal_places=2,
                                            blank=True, null=True, default=0.00)
    net_profit_cost_of_sales = models.DecimalField(verbose_name='Отношение чистой прибыли к стоимости продаж',
                                                   max_digits=32, decimal_places=2, blank=True, null=True, default=0.00)
    revenues_current_assets = models.DecimalField(verbose_name='Отношение выручки к текущим активам', max_digits=32,
                                                  decimal_places=2, blank=True, null=True, default=0.00)
    total_liabilities_this_year_total_liabilities_previous_year = models.DecimalField(
        verbose_name='Общие обязательства / Общие обязательства (пред. год)', max_digits=32, decimal_places=2,
        blank=True, null=True, default=0.00)

    class Meta:
        verbose_name = 'Отчет Oliver Wyman'
        verbose_name_plural = 'Отчеты Oliver Wyman'
