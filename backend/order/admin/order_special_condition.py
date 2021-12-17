from django.contrib import admin
from ..models import OrderSpecialCondition


@admin.register(OrderSpecialCondition)
class OrderSpecialConditionAdmin(admin.ModelAdmin):
    pass
