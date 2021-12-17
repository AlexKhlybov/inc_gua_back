from django.contrib import admin
from ..models import Factors


@admin.register(Factors)
class FactorsAdmin(admin.ModelAdmin):
    pass
