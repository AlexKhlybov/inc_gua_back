from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..models import LegalEntity


@admin.register(LegalEntity)
class LegalEntityAdmin(admin.ModelAdmin):
    ordering = ('inn',)
    list_display = ('title', 'other_title', 'type', 'taxation', 'inn', 'kpp')

    def get_fieldsets(self, request, obj=None):
        return (
            (None, {'fields': (
                'title', 'other_title', 'type', 'taxation', 'inn', 'kpp', 'registration_date', 'registration_address',
                'actual_address', 'region', 'okved', 'opf', 'average_number_of_employees', 'regulation_document',
                'attorney_document', 'no_audit'
            )}),
            (_('Bank info'), {'fields': (
                'bank_number', 'bank_name', 'bank_inn', 'bank_bik', 'bank_kpp', 'bank_correspondent_account_cb',
            )}),
            (None, {'fields': (
                'fl', 'eio', 'eio_date', 'lpr', 'lpr_post', 'auditor', 'auditor_opinion',
            )}),
        )
