from modeltranslation.translator import TranslationOptions, register
from ...models.pages import ChangePassword


@register(ChangePassword)
class ChangePasswordTranslationOptions(TranslationOptions):
    pass
