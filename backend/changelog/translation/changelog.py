from modeltranslation.translator import TranslationOptions, register

from ..models import ChangeLog


@register(ChangeLog)
class ChangeLogTranslationOptions(TranslationOptions):
    pass
