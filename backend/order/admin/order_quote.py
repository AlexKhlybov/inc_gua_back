from django.contrib import admin

from ..models.order_quote import OrderQuote


@admin.register(OrderQuote)
class OrderQuoteAdmin(admin.ModelAdmin):
    pass
