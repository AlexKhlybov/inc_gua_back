from modeltranslation.translator import TranslationOptions, register
from ...models import OrderQuotationPage


@register(OrderQuotationPage)
class OrderQuotationPageTranslationOptions(TranslationOptions):
    pass
