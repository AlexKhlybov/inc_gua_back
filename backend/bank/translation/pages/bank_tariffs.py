from modeltranslation.translator import TranslationOptions, register
from ...models import BankTariffsPage


@register(BankTariffsPage)
class BankTariffsPageTranslationOptions(TranslationOptions):
    pass
