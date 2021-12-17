from django.contrib import admin
from ..models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    pass
