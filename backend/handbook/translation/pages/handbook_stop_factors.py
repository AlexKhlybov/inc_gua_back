from modeltranslation.translator import TranslationOptions, register
from ...models import HandbookStopFactorsPage


@register(HandbookStopFactorsPage)
class HandbookStopFactorsPageTranslationOptions(TranslationOptions):
    pass
