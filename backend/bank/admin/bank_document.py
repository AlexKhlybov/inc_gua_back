from django.contrib import admin
from ..models import BankDocument


@admin.register(BankDocument)
class BankDocumentAdmin(admin.ModelAdmin):
    pass
