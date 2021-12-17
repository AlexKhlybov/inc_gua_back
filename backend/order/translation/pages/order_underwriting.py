from modeltranslation.translator import TranslationOptions, register
from ...models import OrderUnderwritingPage


@register(OrderUnderwritingPage)
class OrderUnderwritingPageTranslationOptions(TranslationOptions):
    pass
