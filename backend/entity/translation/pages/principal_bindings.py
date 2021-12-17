from modeltranslation.translator import TranslationOptions, register
from ...models import PrincipalBindingsPage


@register(PrincipalBindingsPage)
class PrincipalBindingsPageTranslationOptions(TranslationOptions):
    pass
