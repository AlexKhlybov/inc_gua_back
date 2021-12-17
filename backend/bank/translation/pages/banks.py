from modeltranslation.translator import TranslationOptions, register
from ...models import BanksPage


@register(BanksPage)
class BanksPageTranslationOptions(TranslationOptions):
    pass
