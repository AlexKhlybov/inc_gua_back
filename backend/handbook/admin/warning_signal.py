from django.contrib import admin
from ..models import WarningSignal


@admin.register(WarningSignal)
class WarningSignalAdmin(admin.ModelAdmin):
    pass
