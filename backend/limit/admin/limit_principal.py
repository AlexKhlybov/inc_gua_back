from django.contrib import admin
from limit.models import LimitPrincipalModel


@admin.register(LimitPrincipalModel)
class LimitPrincipalModelAdmin(admin.ModelAdmin):
    readonly_fields = ['free_balance', ]
