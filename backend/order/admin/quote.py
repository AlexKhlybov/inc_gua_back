from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..models.quote import Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    readonly_fields = ['bank_commission', 'insurance_premium_commission', 'master_agent_commission',
                       'agent_commission', ]

    def get_fieldsets(self, request, obj=None):
        return (
            (None, {'fields': ('auction', 'bank', 'guarantee_rate', 'guarantee_sum', 'total_commission', 'type',
                               'status', 'expiry_date')}),
            (_('Bank'),
                {'fields': ('bank_rate', 'bank_sum', 'bank_commission',)}),
            (_('Insurance premium'), {
                'fields': ('insurance_premium_rate', 'insurance_premium_sum', 'insurance_premium_commission', ),
            }),
            (_('Master-agent'), {
                'fields': ('master_agent_rate', 'master_agent_sum', 'master_agent_commission', ),
            }),
            (_('Agent'), {'fields': ('agent_rate', 'agent_sum', 'agent_commission', )}))
