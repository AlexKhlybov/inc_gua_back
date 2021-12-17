from modeltranslation.translator import TranslationOptions, register
from ...models import OrderPurchasePage


@register(OrderPurchasePage)
class OrderPurchasePageTranslationOptions(TranslationOptions):
    pass
