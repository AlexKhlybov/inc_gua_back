from modeltranslation.translator import TranslationOptions, register
from ...models import PortfolioPage


@register(PortfolioPage)
class PortfolioPageTranslationOptions(TranslationOptions):
    pass
