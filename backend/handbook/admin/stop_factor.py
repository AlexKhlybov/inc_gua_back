from django.contrib import admin
from ..models import StopFactor


@admin.register(StopFactor)
class StopFactorAdmin(admin.ModelAdmin):
    pass
