from ...models import OrderHistoryPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(OrderHistoryPage)
class OrderHistoryPageAdmin(BasePageAdmin):
    pass
