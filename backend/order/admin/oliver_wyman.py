from django.contrib import admin
from ..models import OliverWymanModel


@admin.register(OliverWymanModel)
class OliverWymanAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'customer', 'reportType', 'purchaseNumber')
    list_filter = ('supplier', 'customer')
    save_on_top = True
    fieldsets = (
        (None, {
            'fields': (('supplier', 'customer', 'reportType', 'purchaseNumber'), )
        }),
        ('Модуль бальной метрики', {
            'classes': ('open', ),
            'fields': (('finance_module', 'qualitative_module', 'tenders_module', 'courts_module', 'executory_module',
                        'signals_module', 'pd_pit', 'pd_ttc'))
        }),
        ('Модуль финансовых показателей', {
            'classes': ('open', ),
            'fields': (('capital_assets', 'dynamics_of_revenue_year_to_year', 'EBITDA_short_term_debt_cash_and_interest_payments',
                        'EBITDA_total_liabilities', 'instant_liquidity', 'net_profit_cost_of_sales',
                        'revenues_current_assets', 'total_liabilities_this_year_total_liabilities_previous_year'))
        }),
        ('Модуль сигналов', {
            'classes': ('collapse', ),
            'fields': (('signals_BS_1', 'signals_BS_2', 'signals_BS_5', 'signals_BS_6', 'signals_BS_7', 'signals_BS_10',
                        'signals_BS_14', 'signals_BS_15', 'signals_BS_16', 'signals_BS_18', 'signals_BS_22',
                        'signals_BS_23', 'signals_BS_111', 'signals_GS_0'))
        }),
        ('Модуль арбитражных судов', {
            'classes': ('open', ),
            'fields': (('courts_1', 'courts_2', 'courts_3', 'courts_4', 'courts_5', 'courts_6'))
        }),
        ('Модуль исполнительного производства', {
            'classes': ('open',),
            'fields': (('executory_1', 'executory_2'))
        }),
        ('Модуль тендеров', {
            'classes': ('open',),
            'fields': (('tenders_1', 'tenders_2', 'tenders_3', 'tenders_4'))
        }),
    )
