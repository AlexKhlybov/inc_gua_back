from modeltranslation.translator import TranslationOptions, register
from ...models import PrincipalDocumentsPage


@register(PrincipalDocumentsPage)
class PrincipalDocumentsPageTranslationOptions(TranslationOptions):
    pass
