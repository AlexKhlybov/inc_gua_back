from ...models import HandbookWarningSignalsPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(HandbookWarningSignalsPage)
class HandbookWarningSignalsPageAdmin(BasePageAdmin):
    pass
