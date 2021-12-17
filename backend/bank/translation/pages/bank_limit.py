from modeltranslation.translator import TranslationOptions, register
from ...models import BankLimitPage


@register(BankLimitPage)
class BankLimitPageTranslationOptions(TranslationOptions):
    pass
