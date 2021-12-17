from modeltranslation.translator import TranslationOptions, register
from ...models import HandbookWarningSignalsPage


@register(HandbookWarningSignalsPage)
class HandbookWarningSignalsPageTranslationOptions(TranslationOptions):
    pass
