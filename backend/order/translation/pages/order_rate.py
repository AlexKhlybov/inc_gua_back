from modeltranslation.translator import TranslationOptions, register
from ...models import OrderRatePage


@register(OrderRatePage)
class OrderRatePageTranslationOptions(TranslationOptions):
    pass
