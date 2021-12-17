from decimal import Decimal
from django.db import models

from app.mixins import Timestamps
from .legal_entity import LegalEntity


class Principal(Timestamps):
    title = models.CharField(max_length=256, verbose_name='Название')
    legal_entity = models.ForeignKey(LegalEntity, verbose_name='ЮЛ/ИП', on_delete=models.CASCADE,
                                     related_name='principal_legal_entity',
                                     blank=False, null=False, default=None)

    limit = models.DecimalField(verbose_name='Лимит принципала', max_digits=32, decimal_places=2,
                                default=Decimal('0.00'))

    class Meta:
        verbose_name = 'Принципал'
        verbose_name_plural = 'Принципалы'

    def __str__(self):
        return f'{self.title}'

    def get_financial_indicators(self):
        from order.models import AccountingForm, AccountingFormDetail

        forms = AccountingForm.objects.filter(principal=self)
        if forms:
            data = []
            for form in forms:
                detail_forms = AccountingFormDetail.objects.filter(accounting_form=form)
                equity_capital = detail_forms.filter(code='1300').first()
                non_current_assets = detail_forms.filter(code='1100').first()
                current_assets = detail_forms.filter(code='1200').first()
                amount_of_financial_debt_at_start = detail_forms.filter(code='1410').first()
                amount_of_financial_debt_at_end = detail_forms.filter(code='1510').first()
                liabilities = detail_forms.filter(code='1500').first()
                profit = detail_forms.filter(code='2300').first()
                interest_payable = detail_forms.filter(code='2330').first()
                depreciation = detail_forms.filter(code='1150').first()
                interest_receivable = detail_forms.filter(code='2320').first()
                percents = detail_forms.filter(code='2330').first()
                revenue = detail_forms.filter(code='2110').first()
                year_data = {
                    'year': form.year,
                }
                year_data.update(get_year_extra_data(
                    equity_capital.end_value,
                    non_current_assets.end_value,
                    current_assets.end_value,
                    amount_of_financial_debt_at_start.end_value,
                    amount_of_financial_debt_at_end.end_value,
                    liabilities.end_value,
                    profit.end_value,
                    interest_payable.end_value,
                    depreciation.end_value,
                    interest_receivable.end_value,
                    percents.end_value,
                    revenue,
                ))
                data.append(year_data)
            return data
        return None


def get_year_extra_data(equity_capital, non_current_assets, current_assets,
                        amount_of_financial_debt_at_start, amount_of_financial_debt_at_end,
                        liabilities, profit, interest_payable, depreciation, interest_receivable,
                        percents, revenue):
    """
     Проверяет данные на валидность, в случае валидности считает
    """
    data = {}
    if args_is_valid(equity_capital, non_current_assets, current_assets):
        data.update({'security_of_current_assets': Decimal((equity_capital - non_current_assets) / current_assets)})

    if args_is_valid(amount_of_financial_debt_at_start, amount_of_financial_debt_at_end, equity_capital):
        data.update({'financial_leverage': Decimal(
            (amount_of_financial_debt_at_start + amount_of_financial_debt_at_end) / equity_capital)})

    if args_is_valid(current_assets, liabilities):
        data.update({'current_liquid': Decimal(current_assets / liabilities)})

    if args_is_valid(profit, interest_payable, depreciation, interest_receivable, revenue):
        data.update({'profitability': Decimal((profit + interest_payable + Decimal(
            depreciation * 0.08) - interest_receivable) / revenue.end_value)})

    if args_is_valid(amount_of_financial_debt_at_start, amount_of_financial_debt_at_end, profit, interest_payable,
                     depreciation, interest_receivable):
        data.update({'debt': Decimal((amount_of_financial_debt_at_start + amount_of_financial_debt_at_end) / (
                profit + interest_payable + Decimal(depreciation * 0.08) - interest_receivable))})  # noqa

    if args_is_valid(profit, interest_payable, depreciation, interest_receivable, percents):
        data.update(
            {'service': Decimal(
                (profit + interest_payable + Decimal(depreciation * 0.08) - interest_receivable) / percents)})

    if args_is_valid(revenue.end_value, revenue.start_value):
        data.update({'revenue': Decimal(revenue.end_value / revenue.start_value)})

    return data


def args_is_valid(*args):
    """
    Валидирует данные для подсчетов
    """
    if None in args:
        return False
    return True
