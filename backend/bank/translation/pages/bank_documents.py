from modeltranslation.translator import TranslationOptions, register
from ...models import BankDocumentsPage


@register(BankDocumentsPage)
class BankDocumentsPageTranslationOptions(TranslationOptions):
    pass
