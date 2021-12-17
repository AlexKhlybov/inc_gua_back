from modeltranslation.translator import TranslationOptions, register
from ...models import PrincipalRatePage


@register(PrincipalRatePage)
class PrincipalRatePageTranslationOptions(TranslationOptions):
    pass
