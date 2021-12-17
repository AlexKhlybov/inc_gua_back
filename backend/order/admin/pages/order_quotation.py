from ...models import OrderQuotationPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(OrderQuotationPage)
class OrderQuotationPageAdmin(BasePageAdmin):
    pass
