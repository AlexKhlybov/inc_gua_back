from ...models.pages import UnderwritersPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(UnderwritersPage)
class UnderwritersPageAdmin(BasePageAdmin):
    pass
