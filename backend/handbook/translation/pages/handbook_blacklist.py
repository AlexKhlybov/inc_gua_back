from modeltranslation.translator import TranslationOptions, register
from ...models import HandbookBlacklistPage


@register(HandbookBlacklistPage)
class HandbookBlacklistPageTranslationOptions(TranslationOptions):
    pass
