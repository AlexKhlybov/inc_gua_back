from django.contrib import admin
from ..models import Beneficiary


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'legal_entity', )
