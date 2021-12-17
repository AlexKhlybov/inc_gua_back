from django.contrib import admin
from limit.models import Limit


@admin.register(Limit)
class LimitAdmin(admin.ModelAdmin):
    save_on_top = True
    fieldsets = (
        (None, {
            'fields': (('principal', 'ball_rating', 'delta', 'ball_rating_total', 'letter_rating'), )
        }),
        ('Показатели', {
            'classes': ('open', ),
            'fields': (('financial_indicators', 'work_exp', 'score_big_contracts', 'score_all_contracts', 'score_year',
                        'additional_factors', 'ownership_structure'))
        }),
        ('Допонительные факторы', {
            'classes': ('open',),
            'fields': (('add_factor_1', 'add_factor_2', 'add_factor_3', 'add_factor_4', 'add_factor_5', 'add_factor_6',
                        'add_factor_7', 'add_factor_8', 'add_factor_9'))
        }),
        ('Лимиты', {
            'classes': ('open',),
            'fields': (('limit_fz', 'limit_bank', 'limit_principal'))
        }),
    )
