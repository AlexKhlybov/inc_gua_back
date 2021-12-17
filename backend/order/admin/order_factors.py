from django.contrib import admin
from ..models import OrderFactors


@admin.register(OrderFactors)
class OrderFactorsAdmin(admin.ModelAdmin):
    pass
