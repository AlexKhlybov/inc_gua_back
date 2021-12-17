from modeltranslation.translator import TranslationOptions, register
from ...models import OrderHistoryPage


@register(OrderHistoryPage)
class OrderHistoryPageTranslationOptions(TranslationOptions):
    pass
