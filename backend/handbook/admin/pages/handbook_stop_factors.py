from ...models import HandbookStopFactorsPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(HandbookStopFactorsPage)
class HandbookStopFactorsPageAdmin(BasePageAdmin):
    pass
