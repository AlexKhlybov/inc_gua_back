import datetime
import io
import logging
import os
import random
import string
from decimal import Decimal
from pathlib import Path

from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.signals import post_delete, post_save
from django.db import models
from django.utils.timezone import now
from django_fsm import FSMField, transition, RETURN_VALUE
from django_fsm_log.decorators import fsm_log_by, fsm_log_description
from django.core.validators import RegexValidator

from app.mixins import Timestamps
from django.dispatch import receiver
from entity.models import Beneficiary, Principal
from garpix_notify.utils import get_file_path
from garpixcms.settings import STATIC_ROOT
from reportlab.lib import colors
from reportlab.lib.colors import black
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame, Paragraph

from .guaranty import Guaranty
from .order_staus import OrderStatus
from changelog.signals import journal_delete_handler, journal_save_handler
from changelog.mixins import ModelDiffMixin
from changelog.middleware import LoggedInUser

STATES = (('CREATED', 'Создана'),
          ('SENT', 'Отправлена'),
          ('UNDERWRITING_A_NEW_APPLICATION', 'Андеррайтинг новая заявка'),
          ('UNDERWRITING_IN_PROGRESS', 'Андеррайтинг в работе'),
          ('UNDERWRITING_REQUERY', 'Андеррайтинг дозапрос'),
          ('UNDERWRITING_REFUSAL', 'Андеррайтинг отказ'),

          ('QUOTE_AUTO', 'Котировка авто'),
          ('QUOTE_AUCTION', 'Котировка торг'),
          ('QUOTE_INDIVIDUAL', 'Котировка индивид'),
          ('QUOTE_SENT', 'Котировка направлена'),
          ('QUOTE_REDEFINED', 'Котировка предоставлена'),
          ('QUOTE_REFUSAL', 'Котировка отказ'),
          ('QUOTE_AGREED', 'Котировка согласована'),

          ('DOCUMENTS_REQUERY', 'Документы дозапрос'),
          ('DOCUMENTS_SIGNATURE', 'Документы подпись'),
          ('DOCUMENTS_REFUSAL', 'Документы отказ'),

          ('GUARANTEE_ISSUE_REQUESTED', 'Выпуск гарантии запрошен'),
          ('GUARANTEE_ISSUED_PAYMENT_EXPECTED', 'Гарантия выпущена ожидается оплата'),
          ('GUARANTEE_DISCLAIMER', 'Выпуск гарантии отказ'),
          ('GUARANTEE_VALID', 'Гарантия действующая'),
          ('GUARANTEE_BENEFICIARY_CLAIM_RECEIVED', 'Гарантия получено требование бенефицара'),
          ('GUARANTEE_LATE_PAYMENT_COMMISSION', 'Гарантия просрочка уплаты комиссии'),
          ('GUARANTEE_PAYMENT_MADE_BENEFICIARY', 'Гарантия произведена выплата бенефициару'),
          ('GUARANTEE_RECOURSE_CLAIM_MADE_AGAINST_PRINCIPAL', 'Гарантия предъявлено регрессное требование принципалу'),
          ('GUARANTEE_CLAIM_PAYMENT_INSURANCE_COMPENSATION',
           'Гарантия предъявлено требование на выплату страхового возмещения'),
          ('GUARANTEE_EXPIRED', 'Гарантия истек срок действия'),
          ('GUARANTEE_PAYMENT_INSURANCE_COMPENSATION_MADE', 'Гарантия произведена выплата страхового возмещения'),
          ('GUARANTEE_TERMINATED', 'Гарантия прекращена'),

          ('IN_ARCHIVE', 'Заявки в архиве')
          )


class Order(Timestamps, ModelDiffMixin):
    class TYPEGUARANTEE:
        ADVANCE = 'Аванс'
        TENDER = 'На участие в тендере'
        CONTRACT = 'На исполнение контракта'
        TYPES = (
            (ADVANCE, 'Аванс'),
            (TENDER, 'На участие в тендере'),
            (CONTRACT, 'На исполнение контракта'),
        )

    class STATUS:
        BLANK = 'Blank'
        SOMETHING = 'Something'
        DONE = 'Done'
        STATES = (
            (BLANK, 'Blank'),
            (SOMETHING, 'Something'),
            (DONE, 'Done'),
        )

    class TYPEDOC:
        ORDER = 'Order'
        GUARANTEE = 'Guarantee'
        TYPES = (
            (ORDER, 'Order'),
            (GUARANTEE, 'Guarantee'),
        )

    status_state = models.CharField(max_length=10, choices=STATUS.STATES,
                                    blank=True, default='Blank')
    status_retries_count = models.IntegerField(default=0)

    doc_type = models.CharField(max_length=100, verbose_name='Тип документа', choices=TYPEDOC.TYPES,
                                blank=True, default='Order')
    state = FSMField(default='CREATED', choices=STATES)

    status = models.ForeignKey(OrderStatus, verbose_name='Статус', blank=True, null=True, default=None,
                               on_delete=models.SET_DEFAULT, related_name='status')
    principal = models.ForeignKey(Principal, verbose_name='Принципал', null=True,
                                  on_delete=models.SET_NULL, related_name='principal_orders')
    beneficiary = models.ForeignKey(Beneficiary, verbose_name='Бенефициар', null=True, default=None,
                                    on_delete=models.SET_NULL, related_name='beneficiary_orders')
    sum = models.DecimalField(verbose_name='Сумма', blank=True, max_digits=32, decimal_places=2,
                              default=Decimal('0.00'))
    guarantee_type = models.CharField(max_length=100, verbose_name='Тип гарантии', choices=TYPEGUARANTEE.TYPES,
                                      blank=True, default='Аванс')
    guaranty = models.ForeignKey(Guaranty, verbose_name='Гарантия', blank=True, null=True, default=None,
                                 on_delete=models.SET_DEFAULT, related_name='guaranty_order')
    contest = models.ForeignKey('Contest', verbose_name='Конкурс', blank=True, null=True, default=None,
                                on_delete=models.SET_DEFAULT, related_name='contest_order')
    quote = models.ForeignKey('Quote', verbose_name='Котировка', blank=True, null=True, default=None,
                              on_delete=models.SET_DEFAULT, related_name='quote_order')
    bank = models.ForeignKey('bank.Bank', verbose_name='Банк', blank=True, null=True, default=None,
                             on_delete=models.SET_DEFAULT, related_name='bank_order')
    underwriter = models.ForeignKey('user.User', verbose_name='Андеррайтер', blank=True, null=True, default=None,
                                    on_delete=models.SET_DEFAULT, related_name='underwriter_order')
    pnt = models.CharField(verbose_name='Реестровый номер торгов', max_length=1000, blank=True)
    eis_link = models.CharField(verbose_name='Ссылка на закупку в ЕИС', max_length=1000, blank=True)
    start_date = models.DateField(verbose_name='Дата начала', blank=True, null=True, default=now())
    end_date = models.DateField(verbose_name='Дата окончания', blank=True, null=True)

    term = models.CharField(verbose_name='Срок гарантии(в днях)', blank=True, max_length=1000, validators=[
        RegexValidator(r'^[0-9]*$', 'Значение должно содержать только цифры')], help_text='Пример: 365')
    take_date = models.DateField(verbose_name='Дата получения БГ', blank=True, null=True)
    availability_without_acceptance = models.BooleanField(verbose_name='Наличие права безакцептного списание',
                                                          blank=True, default=False)
    security_under_guarantee = models.BooleanField(verbose_name='Обеспечение по гарантии', blank=True, default=False)
    provision = models.BooleanField(verbose_name='Обеспечение', blank=True, default=False)
    provision_form = models.CharField(verbose_name='Форма обеспечения', blank=True, max_length=1000)
    provision_sum = models.DecimalField(verbose_name='Сумма обеспечения', blank=True, max_digits=32, decimal_places=2,
                                        default=Decimal('0.00'))

    # ПОЛЕ ДЛЯ ЭЦП
    data_to_sign_txt_box = models.TextField(blank=True, default='', verbose_name='ЭЦП данные')
    signature = models.TextField(blank=True, default='', verbose_name='ЭЦП')
    signature_author = models.TextField(blank=True, default='', verbose_name='ЭЦП Автор')
    report_pdf = models.FileField(verbose_name='Решение по запросу', upload_to=get_file_path, blank=True, null=True)
    #

    is_quote_agreed = models.BooleanField(verbose_name='Котировка согласована', default=False)
    in_archive = models.BooleanField(verbose_name='В архиве', default=False)
    uw_has_been_changed = models.BooleanField(verbose_name='Андеррайтер был переназначен', default=False)

    special_condition = models.ManyToManyField('OrderSpecialCondition', verbose_name='Специальные условия', blank=True,
                                               related_name='special_condition_order')

    def get_stop_factors(self):
        from .order_factors import OrderFactors
        qs = OrderFactors.objects.filter(order=self, factors__catalog='STOP', factors__value=True).values('value')
        return any(v for v in iter(qs))

    def get_pre_signals(self):
        from .order_factors import OrderFactors
        qs = OrderFactors.objects.filter(order=self, factors__catalog='FORCED', factors__value=True).values('value')
        return any(v for v in iter(qs))

    def has_signature(self):
        return 'Да' if self.signature != '' else 'Нет'

    has_signature.short_description = 'Подписано ЭЦП'

    @classmethod
    def create_ecp_pdf_file(cls, pk):
        obj = cls.objects.get(pk=pk)
        from ..models.contract import Contract
        purchase_number = Contract.objects.filter(beneficiary=obj.beneficiary.id).last()
        if obj.data_to_sign_txt_box and obj.signature and obj.signature_author:
            field_rows = ['Принципал', 'ИНН', 'Бенефициар', 'ИНН ', 'Номер закупки', 'Вид(ФЗ)', 'Тип Гарантии',
                          'Сумма Бг', 'Дата начала', 'Дата окончания', 'Обеспечение', 'ФИО', 'Дата']
            field_frames = {
                'principal': ' ' if isinstance(obj.principal.title, type(None)) else obj.principal.title,
                'principal_inn': ' ' if isinstance(obj.principal.legal_entity.inn, type(None)) or isinstance(
                    obj.principal.legal_entity, type(None)) or isinstance(obj.principal, type(None)) else str(
                    obj.principal.legal_entity.inn),
                'beneficiary': ' ' if isinstance(obj.beneficiary, type(None)) else str(obj.beneficiary.title),
                'beneficiary_inn': ' ' if isinstance(obj.beneficiary, type(None)) or isinstance(
                    obj.beneficiary.legal_entity, type(None)) else str(obj.beneficiary.legal_entity.inn),
                'purchase_number': ' ' if isinstance(purchase_number, type(None)) or isinstance(
                    purchase_number.purchase, type(None)) or isinstance(purchase_number.purchase.number, type(None))
                else str(purchase_number.purchase.number),
                'fz': ' ' if isinstance(obj.contest, type(None)) or isinstance(obj.contest.fz, type(None)) else str(
                    obj.contest.fz),
                'guaranty_type': ' ' if isinstance(obj.guarantee_type, type(None)) else str(obj.guarantee_type),
                'bg_sum': ' ' if isinstance(obj.guaranty, type(None)) or isinstance(obj.guaranty.sum,
                                                                                    type(None)) else str(
                    obj.guaranty.sum),
                'start_date': ' ' if isinstance(obj.guaranty, type(None)) or isinstance(obj.guaranty.start_date,
                                                                                        type(None)) else str(
                    obj.guaranty.start_date),
                'end_date': ' ' if isinstance(obj.guaranty, type(None)) or isinstance(obj.guaranty.end_date,
                                                                                      type(None)) else str(
                    obj.guaranty.end_date),
                'provision': ' ' if isinstance(obj.guaranty, type(None)) or isinstance(obj.guaranty.provision_sum,
                                                                                       type(None)) else str(
                    obj.guaranty.provision_sum),
                'full_name': ' ' if isinstance(obj.signature_author, type(None)) else str(obj.signature_author),
                'date': str(datetime.date.today())
            }

            fields = {}
            frames = {}
            letters = string.ascii_letters
            filename = obj.guarantee_type + '_' + ''.join(random.choice(letters) for _ in range(64)) + '.pdf' \
                if obj.guarantee_type else obj.principal + '_' + ''.join(
                random.choice(letters) for _ in range(64)) + '.pdf'
            title = obj.guarantee_type
            buffer = io.BytesIO()
            canv = canvas.Canvas(buffer, pagesize=A4)

            try:
                file = Path(f'{STATIC_ROOT}/fonts/times.ttf')
            except FileNotFoundError as err:
                logging.error(err)
            else:
                if file.is_file():
                    pdfmetrics.registerFont(TTFont('Times New Roman', file))
                else:
                    pdfmetrics.registerFont(TTFont('Times New Roman', 'frontend/static/fonts/times.ttf'))

            canv.setTitle(title)
            header = canv.beginText(150, 800)
            header.setFont('Times New Roman', 26)
            header.textLine(f'Решение по запросу № {obj.id}')

            style = ParagraphStyle('Normal', alignment=TA_CENTER, fontName='Times New Roman', borderWidth=1,
                                   borderColor=black,
                                   borderPadding=10, backColor=colors.HexColor('#aeecf2'), leading=4, textColor=black)

            for n, row in enumerate(field_rows, 1):
                fields[row] = canv.beginText(30, 760 - n * 30)

            for key, value in fields.items():
                value.setFont('Times New Roman', 10)
                value.textLine(str(key))
                canv.drawText(value)

            for n, key in enumerate(field_frames.keys(), 1):
                frames[key] = Frame(150, 570 - 30 * n, 400, 200, id=str(field_frames[key]), leftPadding=0,
                                    bottomPadding=2, topPadding=2)

            for key, value in frames.items():
                value.addFromList([Paragraph(field_frames[key], style)], canv)

            canv.drawText(header)
            canv.save()
            content_file = ContentFile(buffer.getvalue())
            file = InMemoryUploadedFile(content_file, 'pdf_file', filename, 'application/pdf', content_file.tell, None)
            return file

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f"{self.principal}"

    def save(self, *args, **kwargs):
        if self.is_quote_agreed:
            self.state = 'QUOTE_AGREED'
        doc_type = 'Guarantee' if self.state in self.get_guarantee_states() or self.state in ['GUARANTEE_DISCLAIMER',
                                                                                              'GUARANTEE_EXPIRED',
                                                                                              'GUARANTEE_TERMINATED'] \
            else 'Order'
        if self.doc_type != doc_type:
            self.doc_type = doc_type
        super(Order, self).save(*args, **kwargs)
        if self.state != 'CREATED':
            return
        try:
            loggedIn = LoggedInUser()
            self.from_created_to_underwriting_a_new_application(by=loggedIn.current_user, description='Создание заявки')
            self.save()
        except Exception:
            print(Exception)

    def can_be_changed(instance):
        """
            Если условие не будет выполнено, то статус заявки не сменится.
        """
        return instance.sum < 1000

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['CREATED'], target='UNDERWRITING_A_NEW_APPLICATION')
    def from_created_to_underwriting_a_new_application(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['UNDERWRITING_A_NEW_APPLICATION', 'UNDERWRITING_REQUERY'],
                target='UNDERWRITING_IN_PROGRESS')
    def to_underwriting_in_progress(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['UNDERWRITING_A_NEW_APPLICATION'], target='UNDERWRITING_A_NEW_APPLICATION')
    def to_underwriting_a_new_application(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['UNDERWRITING_IN_PROGRESS'], target='UNDERWRITING_REQUERY')
    def to_underwriting_requery(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['UNDERWRITING_IN_PROGRESS'], target='QUOTE_AUTO')
    def to_quote_auto(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['UNDERWRITING_IN_PROGRESS'], target='QUOTE_AUCTION')
    def to_quote_auction(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['UNDERWRITING_IN_PROGRESS'], target='QUOTE_INDIVIDUAL')
    def to_quote_individual(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['UNDERWRITING_IN_PROGRESS', 'UNDERWRITING_REQUERY'], target='UNDERWRITING_REFUSAL')
    def to_underwriting_refusal(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['QUOTE_AUTO', 'QUOTE_AUCTION', 'QUOTE_INDIVIDUAL'], target='QUOTE_SENT')
    def to_quote_sent(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state,
                source=['UNDERWRITING_REFUSAL', 'QUOTE_REFUSAL', 'DOCUMENTS_REFUSAL', 'GUARANTEE_DISCLAIMER'],
                target='IN_ARCHIVE')
    def to_in_archive(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['QUOTE_SENT'], target='QUOTE_REDEFINED')
    def to_quote_redefined(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['QUOTE_SENT', 'QUOTE_REDEFINED'], target='QUOTE_REFUSAL')
    def to_quote_refusal(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['QUOTE_REDEFINED'], target='QUOTE_AGREED')
    def to_quote_agreed(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['QUOTE_AGREED'], target='DOCUMENTS_REQUERY')
    def to_documents_requery(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['QUOTE_AGREED', 'DOCUMENTS_REQUERY'], target='DOCUMENTS_SIGNATURE')
    def to_documents_signature(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['DOCUMENTS_REQUERY'], target='DOCUMENTS_REFUSAL')
    def to_documents_refusal(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['DOCUMENTS_SIGNATURE'], target='GUARANTEE_ISSUE_REQUESTED')
    def to_guarantee_issue_requested(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['GUARANTEE_ISSUE_REQUESTED'], target='GUARANTEE_ISSUED_PAYMENT_EXPECTED')
    def to_guarantee_issued_payment_expected(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['GUARANTEE_ISSUE_REQUESTED'], target='GUARANTEE_DISCLAIMER')
    def to_guarantee_disclaimer(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source=['GUARANTEE_ISSUED_PAYMENT_EXPECTED'], target='GUARANTEE_VALID')
    def to_guarantee_valid(self, *args, **kwargs):
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(field=state, source='*', target=RETURN_VALUE(
        'CREATED',
        'SENT',
        'UNDERWRITING_A_NEW_APPLICATION',
        'UNDERWRITING_IN_PROGRESS',
        'UNDERWRITING_REQUERY',
        'UNDERWRITING_REFUSAL',
        'QUOTE_AUTO',
        'QUOTE_AUCTION',
        'QUOTE_INDIVIDUAL',
        'QUOTE_SENT',
        'QUOTE_REDEFINED',
        'QUOTE_REFUSAL',
        'QUOTE_AGREED',
        'DOCUMENTS_REQUERY',
        'DOCUMENTS_SIGNATURE',
        'DOCUMENTS_REFUSAL',
        'GUARANTEE_ISSUE_REQUESTED',
        'GUARANTEE_ISSUED_PAYMENT_EXPECTED',
        'GUARANTEE_DISCLAIMER',
        'GUARANTEE_VALID',
        'GUARANTEE_BENEFICIARY_CLAIM_RECEIVED',
        'GUARANTEE_LATE_PAYMENT_COMMISSION',
        'GUARANTEE_PAYMENT_MADE_BENEFICIARY',
        'GUARANTEE_RECOURSE_CLAIM_MADE_AGAINST_PRINCIPAL',
        'GUARANTEE_CLAIM_PAYMENT_INSURANCE_COMPENSATION',
        'GUARANTEE_EXPIRED',
        'GUARANTEE_PAYMENT_INSURANCE_COMPENSATION_MADE',
        'GUARANTEE_TERMINATED',
        'IN_ARCHIVE'
    ))
    def update_to_state(self, *args, **kwargs):
        return kwargs['state']

    def update_state(self, *args, **kwargs):
        """
            в файле task_transitions отражена диаграмма переходов, генерируется автоматически командой
            python3 manage.py graph_transitions -o task_transitions.png order.Order
        """
        try:
            self.update_to_state(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_underwriting_a_new_application(self, *args, **kwargs):
        try:
            self.to_underwriting_a_new_application(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_underwriting_in_progress(self, *args, **kwargs):
        try:
            self.to_underwriting_in_progress(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_underwriting_requery(self, *args, **kwargs):
        try:
            self.to_underwriting_requery(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_quote_auto(self, *args, **kwargs):
        try:
            self.to_quote_auto(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_quote_auction(self, *args, **kwargs):
        try:
            self.to_quote_auction(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_quote_individual(self, *args, **kwargs):
        try:
            self.to_quote_individual(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_underwriting_refusal(self, *args, **kwargs):
        try:
            self.to_underwriting_refusal(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_quote_sent(self, *args, **kwargs):
        try:
            self.to_quote_sent(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_in_archive(self, *args, **kwargs):
        try:
            self.to_in_archive(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_quote_redefined(self, *args, **kwargs):
        try:
            self.to_quote_redefined(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_quote_refusal(self, *args, **kwargs):
        try:
            self.to_quote_refusal(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_quote_agreed(self, *args, **kwargs):
        try:
            self.to_quote_agreed(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_documents_requery(self, *args, **kwargs):
        try:
            self.to_documents_requery(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_documents_signature(self, *args, **kwargs):
        try:
            self.to_documents_signature(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_documents_refusal(self, *args, **kwargs):
        try:
            self.to_documents_refusal(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_guarantee_issue_requested(self, *args, **kwargs):
        try:
            self.to_guarantee_issue_requested(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_guarantee_issued_payment_expected(self, *args, **kwargs):
        try:
            self.to_guarantee_issued_payment_expected(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_guarantee_disclaimer(self, *args, **kwargs):
        try:
            self.to_guarantee_disclaimer(*args, **kwargs)
        except Exception:
            print(Exception)

    def to_state_guarantee_valid(self, *args, **kwargs):
        try:
            self.to_guarantee_valid(*args, **kwargs)
        except Exception:
            print(Exception)

    @staticmethod
    def get_order_states():
        states = []
        states.append('CREATED')
        states.append('SENT')
        states.append('UNDERWRITING_A_NEW_APPLICATION')
        states.append('UNDERWRITING_IN_PROGRESS')
        states.append('UNDERWRITING_REQUERY')
        states.append('QUOTE_AUTO')
        states.append('QUOTE_AUCTION')
        states.append('QUOTE_INDIVIDUAL')
        states.append('QUOTE_SENT')
        states.append('QUOTE_REDEFINED')
        states.append('QUOTE_AGREED')
        states.append('DOCUMENTS_REQUERY')
        states.append('DOCUMENTS_SIGNATURE')
        states.append('GUARANTEE_ISSUE_REQUESTED')
        states.append('GUARANTEE_ISSUED_PAYMENT_EXPECTED')
        return states

    @staticmethod
    def get_guarantee_states():
        states = []
        states.append('GUARANTEE_VALID')
        states.append('GUARANTEE_BENEFICIARY_CLAIM_RECEIVED')
        states.append('GUARANTEE_LATE_PAYMENT_COMMISSION')
        states.append('GUARANTEE_PAYMENT_MADE_BENEFICIARY')
        states.append('GUARANTEE_RECOURSE_CLAIM_MADE_AGAINST_PRINCIPAL')
        states.append('GUARANTEE_CLAIM_PAYMENT_INSURANCE_COMPENSATION')
        states.append('GUARANTEE_PAYMENT_INSURANCE_COMPENSATION_MADE')
        return states

    @staticmethod
    def get_all_states():
        states = []
        states.append('CREATED')
        states.append('SENT')
        states.append('UNDERWRITING_A_NEW_APPLICATION')
        states.append('UNDERWRITING_IN_PROGRESS')
        states.append('UNDERWRITING_REQUERY')
        states.append('UNDERWRITING_REFUSAL')
        states.append('QUOTE_AUTO')
        states.append('QUOTE_AUCTION')
        states.append('QUOTE_INDIVIDUAL')
        states.append('QUOTE_SENT')
        states.append('QUOTE_REDEFINED')
        states.append('QUOTE_REFUSAL')
        states.append('QUOTE_AGREED')
        states.append('DOCUMENTS_REQUERY')
        states.append('DOCUMENTS_SIGNATURE')
        states.append('DOCUMENTS_REFUSAL')
        states.append('GUARANTEE_ISSUE_REQUESTED')
        states.append('GUARANTEE_ISSUED_PAYMENT_EXPECTED')
        states.append('GUARANTEE_DISCLAIMER')
        states.append('GUARANTEE_VALID')
        states.append('GUARANTEE_BENEFICIARY_CLAIM_RECEIVED')
        states.append('GUARANTEE_LATE_PAYMENT_COMMISSION')
        states.append('GUARANTEE_PAYMENT_MADE_BENEFICIARY')
        states.append('GUARANTEE_RECOURSE_CLAIM_MADE_AGAINST_PRINCIPAL')
        states.append('GUARANTEE_CLAIM_PAYMENT_INSURANCE_COMPENSATION')
        states.append('GUARANTEE_EXPIRED')
        states.append('GUARANTEE_PAYMENT_INSURANCE_COMPENSATION_MADE')
        states.append('GUARANTEE_TERMINATED')
        states.append('IN_ARCHIVE')
        return states


post_save.connect(journal_save_handler, sender=Order)
post_delete.connect(journal_delete_handler, sender=Order)


@receiver(post_save, sender=Order)
def create_pdf(sender, instance, **kwargs):
    if instance.data_to_sign_txt_box and instance.signature and instance.signature_author:
        file = sender.create_ecp_pdf_file(instance.id)
        if isinstance(instance.report_pdf, type(None)):
            instance.report_pdf = file
        else:
            try:
                os.remove(instance.report_pdf.path)
            except Exception as err:
                print(err)
            finally:
                instance.report_pdf = file
    post_save.disconnect(create_pdf, sender=Order)
    instance.save()
    post_save.connect(create_pdf, sender=Order)
