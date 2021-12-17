from modeltranslation.translator import TranslationOptions, register
from ...models.pages import UnderwritersPage


@register(UnderwritersPage)
class UnderwritersPageTranslationOptions(TranslationOptions):
    pass
