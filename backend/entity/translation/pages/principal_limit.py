from modeltranslation.translator import TranslationOptions, register
from ...models import PrincipalLimitPage


@register(PrincipalLimitPage)
class PrincipalLimitPageTranslationOptions(TranslationOptions):
    pass
