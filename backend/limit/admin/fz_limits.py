from django.contrib import admin
from ..models import FZLimits


@admin.register(FZLimits)
class FZLimitsAdmin(admin.ModelAdmin):
    readonly_fields = ['free_balance', ]
