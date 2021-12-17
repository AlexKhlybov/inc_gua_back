from django.contrib import admin
from ..models import ContestType


@admin.register(ContestType)
class ContestTypeAdmin(admin.ModelAdmin):
    pass
