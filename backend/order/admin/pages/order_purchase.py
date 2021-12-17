from ...models import OrderPurchasePage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(OrderPurchasePage)
class OrderPurchasePageAdmin(BasePageAdmin):
    pass
