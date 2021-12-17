from django.contrib import admin
from ..models import LimitBank


@admin.register(LimitBank)
class LimitBankAdmin(admin.ModelAdmin):
    pass
