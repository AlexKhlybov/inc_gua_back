from ...models import BankDocumentsPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(BankDocumentsPage)
class BankDocumentsPageAdmin(BasePageAdmin):
    pass
