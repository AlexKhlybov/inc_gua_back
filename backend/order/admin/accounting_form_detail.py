from django.contrib import admin
from ..models import AccountingFormDetail


@admin.register(AccountingFormDetail)
class AccountingFormDetailAdmin(admin.ModelAdmin):
    pass
