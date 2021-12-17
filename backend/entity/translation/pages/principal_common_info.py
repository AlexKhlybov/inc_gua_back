from modeltranslation.translator import TranslationOptions, register
from ...models import PrincipalCommonInfoPage


@register(PrincipalCommonInfoPage)
class PrincipalCommonInfoPageTranslationOptions(TranslationOptions):
    pass
