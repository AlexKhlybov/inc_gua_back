from ...models import OrderQuotationTradePage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(OrderQuotationTradePage)
class OrderQuotationTradePageAdmin(BasePageAdmin):
    pass
