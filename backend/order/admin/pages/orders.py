from ...models import OrdersPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(OrdersPage)
class OrdersPageAdmin(BasePageAdmin):
    pass
