from modeltranslation.translator import TranslationOptions, register
from ...models import PrincipalFinancialReportPage


@register(PrincipalFinancialReportPage)
class PrincipalFinancialReportPageTranslationOptions(TranslationOptions):
    pass
