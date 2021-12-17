from modeltranslation.translator import TranslationOptions, register
from ...models import OrderDocumentsPage


@register(OrderDocumentsPage)
class OrderDocumentsPageTranslationOptions(TranslationOptions):
    pass
