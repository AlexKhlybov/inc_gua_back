from django.db import models

from app.mixins import Timestamps


class Factors(Timestamps):
    class TYPE:
        # Принципал
        PERIOD_OF_ACTIVITY = 'Срок деятельности'
        USRoLE_REGISTRATION = 'ЕГРЮЛ / Регистрация'
        USRoLE_REORGANIZATION = 'ЕГРЮЛ / Реорганизация'
        USRoLE_INVALID = 'ЕГРЮЛ / Недействующее'
        USRoLE_UNIQUENESS = 'ЕГРЮЛ / Уникальность'
        SUSPENSION_OF_ACTIVITY = 'Приостановка деятельности'
        LIQUIDATION_BANKRUPTCY = 'Ликвидация / Банкротство'
        LIQUIDATION_BANKRUPTCY_OF_PARTICIPANTS = 'Ликвидация / Банкротство участников'
        LIQUIDATION_BANKRUPTCY_STATEMENT = 'Заявление о намерении'
        LIST_OF_TERRORISTS_EXTREMISTS = 'Список террористов/экстремистов'
        LIST_OF_WEAPONS = 'Список с оружием'
        UNRELIABLE_FOREIGN_TRADE_PARTICIPANT = 'Неблагонадежный участник ВЭД'
        UNRELIABLE_INFO_IN_THE_USRoLE = 'Недостоверная инфо в ЕГРЮЛ'
        MASS_REGISTRATION = 'Массовая регистрация'
        MASS_LEADER = 'Список "массовых" руководителей, учредителей'
        ARREARS_OF_TAXES_AND_FEES = 'Задолженность по налогам и сборам'
        PO_ARREARS = 'Задолженность по ЗП'
        BLOCKING_ACCOUNTS = 'Блокировка счетов'
        RNP = 'РНП'
        SHAREHOLDER_VALIDITY_OF_PASSPORT = 'Акционер Действительность паспортов'
        DISQUALIFIED_PERSONS = 'Дисквалифицированные лица'
        SHAREHOLDER_LACK_OF_CITIZENSHIP_OF_THE_RF = 'Акционер Отсутствие гражданства РФ'
        LACK_OF_REGISTRATION_IN_THE_RF = 'Отсутствие регистрации в РФ'
        ENFORCEMENT_PROCEEDINGS = 'Исполнительные производства'
        ARBITRATION = 'Арбитражи'
        GC_EXPERIENCE = 'Опыт ГК'
        TERRITORY_AT_RISK = 'Территория с риском'
        AGE_OF_THE_EIO_IP = 'Возраст ЕИО / ИП'
        THE_SIGNATORY_IS_NOT_AN_EIO = 'Подписант не ЕИО'
        DEBT_ON_BG = 'Задолженность по БГ'
        BIG_DEAL = 'Крупная сделка'
        FREQUENT_CHANGE_OF_THE_EIO = 'Частая смена ЕИО'
        FREQUENT_CHANGE_OF_THE_TAX_AUTHORITY = 'Частая смена налогового органа'
        BLACKLIST = 'Черный список'

        # Отчетность
        SUSPENSION_OF_ACTIVITY_REPORTING = 'Приостановка деятельности'
        NO_ANNUAL_BO = 'Отсутствие годовой БО'
        RELIABILITY = 'Достоверность'
        NEGATIVE_CHA = 'Отрицательные ЧА'
        LOSSES = 'Убытки'
        DECREASE_IN_REVENUE = 'Снижение выручки'
        DZ_KZ_GROWTH = 'Рост ДЗ/КЗ'
        OVERDUE_D_KZ = 'Просроченная ДЗ / КЗ'
        CHA = 'ЧА'
        NON_COMPLIANCE_OF_THE_CONTRACT_WITH_REVENUE = 'Несоответствие контракта выручке'

        # Контракт
        TERRITORY_AT_RISK_CONTRACT = 'Территория с риском Контракт'
        PRODUCT_COMPLIANCE_LAW = 'Соответствие продукту (закон)'
        RESTRICTIONS = 'Ограничения'
        REGIONS = 'Регионы'
        RESTRICTIONS_REPORTING = 'Ограничения'

        # Бенецифар
        TERRITORY_AT_RISK_BENECIFAR = 'Территория с риском'
        PARTICIPANTS_OPK = 'Участники (ОПК)'

        # Лимит / БГ
        LIMIT_ON_THE_PRINCIPAL_CUMULATION = 'Лимит на Принципала/Кумуляция'
        AMOUNT = 'Сумма'
        TERM = 'Срок'
        PRODUCT_COMPLIANCE_TYPE = 'Соответствие продукту (вид)'
        WARRANTY_FOR_RENEWAL = 'Гарантия на продление'
        REPLACEMENT_OF_THE_DEPOSIT = 'Замена депозита'

        TYPES = (
            (PERIOD_OF_ACTIVITY, 'Срок деятельности'),
            (USRoLE_REGISTRATION, 'ЕГРЮЛ / Регистрация'),
            (USRoLE_REORGANIZATION, 'ЕГРЮЛ / Реорганизация'),
            (USRoLE_INVALID, 'ЕГРЮЛ / Недействующее'),
            (USRoLE_UNIQUENESS, 'ЕГРЮЛ / Уникальность'),
            (SUSPENSION_OF_ACTIVITY, 'Приостановка деятельности'),
            (LIQUIDATION_BANKRUPTCY, 'Ликвидация / Банкротство'),
            (LIQUIDATION_BANKRUPTCY_OF_PARTICIPANTS, 'Ликвидация / Банкротство участников'),
            (LIQUIDATION_BANKRUPTCY_STATEMENT, 'Заявление о намерении'),
            (LIST_OF_TERRORISTS_EXTREMISTS, 'Список террористов/экстремистов'),
            (LIST_OF_WEAPONS, 'Список с оружием'),
            (UNRELIABLE_FOREIGN_TRADE_PARTICIPANT, 'Неблагонадежный участник ВЭД'),
            (UNRELIABLE_INFO_IN_THE_USRoLE, 'Недостоверная инфо в ЕГРЮЛ'),
            (MASS_REGISTRATION, 'Массовая регистрация'),
            (MASS_LEADER, 'Список "массовых" руководителей, учредителей'),
            (ARREARS_OF_TAXES_AND_FEES, 'Задолженность по налогам и сборам'),
            (PO_ARREARS, 'Задолженность по ЗП'),
            (BLOCKING_ACCOUNTS, 'Блокировка счетов'),
            (RNP, 'РНП'),
            (SHAREHOLDER_VALIDITY_OF_PASSPORT, 'Акционер Действительность паспортов'),
            (DISQUALIFIED_PERSONS, 'Дисквалифицированные лица'),
            (SHAREHOLDER_LACK_OF_CITIZENSHIP_OF_THE_RF, 'Акционер Отсутствие гражданства РФ'),
            (LACK_OF_REGISTRATION_IN_THE_RF, 'Отсутствие регистрации в РФ'),
            (ENFORCEMENT_PROCEEDINGS, 'Исполнительные производства'),
            (ARBITRATION, 'Арбитражи'),
            (GC_EXPERIENCE, 'Опыт ГК'),
            (TERRITORY_AT_RISK, 'Территория с риском'),
            (AGE_OF_THE_EIO_IP, 'Возраст ЕИО / ИП'),
            (THE_SIGNATORY_IS_NOT_AN_EIO, 'Подписант не ЕИО'),
            (DEBT_ON_BG, 'Задолженность по БГ'),
            (BIG_DEAL, 'Крупная сделка'),
            (FREQUENT_CHANGE_OF_THE_EIO, 'Частая смена ЕИО'),
            (FREQUENT_CHANGE_OF_THE_TAX_AUTHORITY, 'Частая смена налогового органа'),
            (BLACKLIST, 'Черный список'),
            (SUSPENSION_OF_ACTIVITY_REPORTING, 'Приостановка деятельности'),
            (NO_ANNUAL_BO, 'Отсутствие годовой БО'),
            (RELIABILITY, 'Достоверность'),
            (NEGATIVE_CHA, 'Отрицательные ЧА'),
            (LOSSES, 'Убытки'),
            (DECREASE_IN_REVENUE, 'Снижение выручки'),
            (DZ_KZ_GROWTH, 'Рост ДЗ/КЗ'),
            (OVERDUE_D_KZ, 'Просроченная ДЗ / КЗ'),
            (CHA, 'ЧА'),
            (NON_COMPLIANCE_OF_THE_CONTRACT_WITH_REVENUE, 'Несоответствие контракта выручке'),
            (TERRITORY_AT_RISK_CONTRACT, 'Территория с риском Контракт'),
            (PRODUCT_COMPLIANCE_LAW, 'Соответствие продукту (закон)'),
            (RESTRICTIONS, 'Ограничения'),
            (REGIONS, 'Регионы'),
            (RESTRICTIONS_REPORTING, 'Ограничения'),
            (TERRITORY_AT_RISK_BENECIFAR, 'Территория с риском'),
            (PARTICIPANTS_OPK, 'Участники (ОПК)'),
            (LIMIT_ON_THE_PRINCIPAL_CUMULATION, 'Лимит на Принципала/Кумуляция'),
            (AMOUNT, 'Сумма'),
            (TERM, 'Срок'),
            (PRODUCT_COMPLIANCE_TYPE, 'Соответствие продукту (вид)'),
            (WARRANTY_FOR_RENEWAL, 'Гарантия на продление'),
            (REPLACEMENT_OF_THE_DEPOSIT, 'Замена депозита'),
        )

    class CATALOG:
        STOP = 'STOP'
        FORCED = 'FORCED'
        PASSPORT_PRODUCT = 'PASSPORT_PRODUCT'

        TYPES = (
            (STOP, 'STOP'),
            (FORCED, 'FORCED'),
            (PASSPORT_PRODUCT, 'PASSPORT_PRODUCT'),
        )

    catalog = models.CharField('Каталог', max_length=255, choices=CATALOG.TYPES, blank=True)
    type = models.CharField('Вид', max_length=255, choices=TYPE.TYPES, blank=True)
    title = models.CharField(verbose_name='Название', blank=True, max_length=1000)
    value = models.BooleanField(verbose_name='Значение', default=False)

    class Meta:
        verbose_name = 'Фактор'
        verbose_name_plural = 'Факторы'

    def __str__(self):
        return f'{self.title} {self.value}'
