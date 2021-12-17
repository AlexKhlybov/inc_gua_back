from datetime import datetime
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from bank.models import Bank
from entity.models import Principal, Beneficiary, LegalEntity
from limit.models import LimitFZ
from order.models import Contract, OrderSpecialCondition, Order, Quote, DocumentType, \
    OrderDocument
from order.models import ContestType, Lot, Contest, Factors, Auction, Purchase


class BaseTest:
    """
    Класс содержит данные для тестирования
    """

    def __init__(self):
        self.user = get_user_model().objects.create_user(
            email='test@gg.com',
            password='SuPerPasSwOrd12345',
            phone='89969185053',
            is_staff=True,
            is_superuser=True
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.user_agent = get_user_model().objects.create_user(
            email='test_underwriter@gg.com',
            password='SuPerPasSwOrd12345',
            phone='89969185053',
            role='agent',
            is_active=True
        )

        self.client_agent = APIClient()
        self.client_agent.force_authenticate(user=self.user_agent)

        self.user_principal = get_user_model().objects.create_user(
            email='test_principal@gg.com',
            password='SuPerPasSwOrd12345',
            phone='89969185053',
            role='principal',
            is_active=True
        )

        self.client_principal = APIClient()
        self.client_principal.force_authenticate(user=self.user_principal)

        self.user_uw = get_user_model().objects.create_user(
            email='test_uw@gg.com',
            password='SuPerPasSwOrd12345',
            phone='89969185053',
            role='Андеррайтер',
            is_active=True
        )

        self.client_uw = APIClient()
        self.client_uw.force_authenticate(user=self.user_uw)

        self.user_suw = get_user_model().objects.create_user(
            email='test_suw@gg.com',
            password='SuPerPasSwOrd12345',
            phone='89969185053',
            role='Мастер-андеррайтер',
            is_active=True
        )

        self.client_suw = APIClient()
        self.client_suw.force_authenticate(user=self.user_suw)

        self.bad_id = '100t'
        self.bank = Bank.objects.create()
        self.condition = self.create_special('Воля')
        self.legal_entity_principal = LegalEntity.objects.create(
            inn='123456789011',
            region='Иваново',
            okved='15.55.67',
        )
        self.legal_entity_beneficiary = LegalEntity.objects.create(
            inn='123456789012',
            region='Дзержинск',
            okved='15.55.67',
        )

        self.principal = Principal.objects.create(
            title='Петя',
            legal_entity=self.legal_entity_principal,
        )
        self.beneficiary = Beneficiary.objects.create(
            title='Алексей',
            legal_entity=self.legal_entity_beneficiary,
        )
        self.contract = self.create_contract(10000000, 10000000, True, 10000000, 10000000, False, 'qweert1234',
                                             self.beneficiary)
        self.lot = self.create_lot(123)
        self.type = self.create_type_contest('Тест тип')
        self.fz = LimitFZ.objects.create(fz='ФЗ-тест')
        self.contest = self.create_contest(okpd2=12345678, nmck=12345678901)
        self.factors = self.create_factors('Test factors')
        self.pnt = 'pnt'
        self.eis_link = 'https://cool.ru'
        self.purchase = self.create_purchase('123', 'Здание')
        self.create_order = Order.objects.create(
            principal=self.principal,
            beneficiary=self.beneficiary,
            contest=self.contest,
            pnt=self.pnt,
            eis_link=self.eis_link,
            start_date=datetime.now(),
        )
        self.document_type = DocumentType.objects.create(
            title='test type'
        )
        self.create_order_document = OrderDocument.objects.create(
            order=self.create_order,
            document_title='test_doc',
            document_type=self.document_type
        )
        self.auction = self.create_auction(12345)
        self.quote = self.create_quote()

    def create_quote(self):
        quote = Quote.objects.create(
            expiry_date=datetime.now()
        )
        return quote

    def create_contract(self, sum, security_amount, availability_payment, availability_sum, availability_share,
                        treasury_support, number, beneficiary):
        contract = Contract.objects.create(
            sum=sum,
            security_amount=security_amount,
            availability_payment=availability_payment,
            availability_sum=availability_sum,
            availability_share=availability_share,
            treasury_support=treasury_support,
            number=number,
            beneficiary=beneficiary,
        )
        return contract

    def create_lot(self, number):
        lot = Lot.objects.create(
            number=number,
        )
        return lot

    def create_type_contest(self, title):
        type_contest = ContestType.objects.create(
            title=title,
        )
        return type_contest

    def create_contest(self, okpd2, nmck):
        contest = Contest.objects.create(
            lot=self.lot,
            type=self.type,
            contract=self.contract,
            fz=self.fz,
            okpd2=okpd2,
            nmck=nmck
        )
        return contest

    def create_factors(self, title):
        factors = Factors.objects.create(
            title=title
        )
        return factors

    def create_special(self, title):
        special = OrderSpecialCondition.objects.create(
            title=title,
        )
        return special

    def create_auction(self, number):
        auction = Auction.objects.create(
            number=number,
        )
        return auction

    def create_purchase(self, number, purchase_object):
        auction = Purchase.objects.create(
            number=number,
            purchase_object=purchase_object
        )
        return auction
