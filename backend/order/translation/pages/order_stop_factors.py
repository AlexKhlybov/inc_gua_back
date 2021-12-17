from modeltranslation.translator import TranslationOptions, register
from ...models import OrderStopFactorsPage


@register(OrderStopFactorsPage)
class OrderStopFactorsPageTranslationOptions(TranslationOptions):
    pass
