from modeltranslation.translator import TranslationOptions, register
from ...models import OrdersPage


@register(OrdersPage)
class OrdersPageTranslationOptions(TranslationOptions):
    pass
