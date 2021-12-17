from ...models import BanksPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(BanksPage)
class BanksPageAdmin(BasePageAdmin):
    pass
