from modeltranslation.translator import TranslationOptions, register
from ...models import OrderFinancialReportPage


@register(OrderFinancialReportPage)
class OrderFinancialReportPageTranslationOptions(TranslationOptions):
    pass
