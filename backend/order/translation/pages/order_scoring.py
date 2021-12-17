from modeltranslation.translator import TranslationOptions, register
from ...models import OrderScoringPage


@register(OrderScoringPage)
class OrderScoringPageTranslationOptions(TranslationOptions):
    pass
