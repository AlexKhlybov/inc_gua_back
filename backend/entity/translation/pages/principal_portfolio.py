from modeltranslation.translator import TranslationOptions, register
from ...models import PrincipalPortfolioPage


@register(PrincipalPortfolioPage)
class PrincipalPortfolioPageTranslationOptions(TranslationOptions):
    pass
