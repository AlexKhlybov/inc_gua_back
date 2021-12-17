from django.contrib import admin
from ..models import BankСontract


@admin.register(BankСontract)
class BankContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary_protocol_number', 'summary_protocol_date', )
    list_display_links = ('summary_protocol_number', )
