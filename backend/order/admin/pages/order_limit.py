from ...models import OrderLimitPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(OrderLimitPage)
class OrderLimitPageAdmin(BasePageAdmin):
    pass
