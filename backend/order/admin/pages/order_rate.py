from ...models import OrderRatePage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(OrderRatePage)
class OrderRatePageAdmin(BasePageAdmin):
    pass
