from ...models import OrderStopFactorsPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(OrderStopFactorsPage)
class OrderStopFactorsPageAdmin(BasePageAdmin):
    pass
