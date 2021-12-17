from ...models import HandbookBlacklistPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(HandbookBlacklistPage)
class HandbookBlacklistPageAdmin(BasePageAdmin):
    pass
