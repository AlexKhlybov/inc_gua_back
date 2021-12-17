from django.contrib import admin
from ..models import BankTariffMatrix


@admin.register(BankTariffMatrix)
class BankTariffMatrixAdmin(admin.ModelAdmin):
    pass
