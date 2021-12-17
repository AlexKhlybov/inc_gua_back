from modeltranslation.translator import TranslationOptions, register
from ...models import PrincipalCoownersPage


@register(PrincipalCoownersPage)
class PrincipalCoownersPageTranslationOptions(TranslationOptions):
    pass
