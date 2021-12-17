from django.contrib import admin
from django_fsm_log.admin import StateLogInline
from ..models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('state', 'start_date', 'end_date', 'sum', '__str__')
    readonly_fields = ('state', 'status', 'has_signature',)
    inlines = [StateLogInline]
    save_on_top = True
    fieldsets = (
        (None, {
            'fields': (('doc_type', 'state', 'guarantee_type', 'underwriter'))
        }),
        ('Стороны сделки', {
            'classes': ('open', ),
            'fields': (('principal', 'beneficiary', 'sum'))
        }),
        ('Информация', {
            'classes': ('open', ),
            'fields': (('contest', 'quote', 'bank', 'pnt', 'eis_link',
                        'start_date', 'end_date', 'special_condition', 'is_quote_agreed', 'in_archive', 'uw_has_been_changed'))
        }),
        ('Данные гарантии', {
            'classes': ('open', ),
            'fields': (('term', 'take_date', 'availability_without_acceptance',
                        'security_under_guarantee', 'provision', 'provision_form', 'provision_sum'))
        }),
        ('ЭЦП', {
            'classes': ('open', ),
            'fields': (('data_to_sign_txt_box', 'signature', 'signature_author', 'report_pdf'))
        }),
    )
