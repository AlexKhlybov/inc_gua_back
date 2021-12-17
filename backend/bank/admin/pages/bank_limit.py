from ...models import BankLimitPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(BankLimitPage)
class BankLimitPageAdmin(BasePageAdmin):
    pass
