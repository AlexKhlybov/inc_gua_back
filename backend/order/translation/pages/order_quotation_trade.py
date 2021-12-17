from modeltranslation.translator import TranslationOptions, register
from ...models import OrderQuotationTradePage


@register(OrderQuotationTradePage)
class OrderQuotationTradePageTranslationOptions(TranslationOptions):
    pass
