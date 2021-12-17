from ...models import BankTariffsPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(BankTariffsPage)
class BankTariffsPageAdmin(BasePageAdmin):
    pass
