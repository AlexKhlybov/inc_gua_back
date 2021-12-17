from django.contrib import admin
from ..models import BankGuaranteeStatus


@admin.register(BankGuaranteeStatus)
class BankGuaranteeStatusAdmin(admin.ModelAdmin):
    pass
