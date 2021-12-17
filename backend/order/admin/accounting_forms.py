from django.contrib import admin
from ..models import AccountingForm


@admin.register(AccountingForm)
class AccountingFormAdmin(admin.ModelAdmin):
    pass
