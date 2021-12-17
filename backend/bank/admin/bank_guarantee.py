from django.contrib import admin
from ..models import BankGuarantee


@admin.register(BankGuarantee)
class BankGuaranteeAdmin(admin.ModelAdmin):
    # list_display = ['number', 'date', 'sum']
    pass
