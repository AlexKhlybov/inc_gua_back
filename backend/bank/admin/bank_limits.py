from django.contrib import admin
from ..models import BankLimits


@admin.register(BankLimits)
class BankLimitsAdmin(admin.ModelAdmin):
    readonly_fields = ['free_balance', ]
