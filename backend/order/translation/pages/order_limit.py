from modeltranslation.translator import TranslationOptions, register
from ...models import OrderLimitPage


@register(OrderLimitPage)
class OrderLimitPageTranslationOptions(TranslationOptions):
    pass
